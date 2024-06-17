import PyPDF2
from django.shortcuts import render
from .forms import PDFUploadForm
from django.http import HttpResponse
from docx import Document
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from .prompts import *
import openai
import json

api_key = "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"
client = openai.OpenAI(api_key=api_key)

def generate_content(prompt):

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.00000001,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text

def extract_info(resume_text,prompt):
    prompt = f"Given the following resume text: {resume_text}"+prompt
    response_content = generate_content(prompt)
    start_index = response_content.find('{')
    end_index = response_content.rfind('}') + 1
    json_string = response_content[start_index:end_index]
    # Convert the JSON string to a Python dictionary
    extracted_info_json = json.loads(json_string)
    return extracted_info_json

def preprocess_extracted_info(extracted_info):
    def format_item(item):
        if isinstance(item, dict):
            formatted = {}
            for key, value in item.items():
                formatted[key] = format_item(value)
            return formatted
        elif isinstance(item, list):
            return [format_item(subitem) for subitem in item]
        else:
            return item
    
    formatted_info = {}
    for key, value in extracted_info.items():
        if isinstance(value, dict):
            formatted_info[key] = format_item(value)
        elif isinstance(value, list):
            formatted_info[key] = [format_item(item) for item in value]
        else:
            formatted_info[key] = value
    
    return formatted_info

def render_item(item):
    if isinstance(item, str):
        return f"<p>{item}</p>"
    elif isinstance(item, list):
        list_items = ''.join([f"<li class='list-item'>{render_item(subitem)}</li>" for subitem in item])
        return f"<ul>{list_items}</ul>"
    elif isinstance(item, dict):
        dict_items = ''.join([f"<div><span class='subkey'>{subkey}:</span>{render_item(subvalue)}</div>" for subkey, subvalue in item.items()])
        return dict_items
    else:
        return f"<p>{item}</p>"

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            pdf_text = extract_text_from_pdf(pdf_file)

            # Extract information using the prompts
            name_info = extract_info(pdf_text, name_prompt)
            job_info = extract_info(pdf_text, job_prompt)
            soft_info = extract_info(pdf_text, soft_prompt)
            xp_info = extract_info(pdf_text, xp_prompt)
            savoir_info = extract_info(pdf_text, savoir_prompt)
            hard_info = extract_info(pdf_text, hard_prompt)
            
            education_info = extract_info(pdf_text, education_prompt)
            language_info = extract_info(pdf_text, language_prompt)
            certification_info = extract_info(pdf_text, certification_prompt)
            professional_info = extract_info(pdf_text, professional_prompt)
            personal_info = extract_info(pdf_text, personal_project_prompt)

            # Construct the new dictionary
            extracted_info = {
                'Trigramme': name_info['firstName'][0] + name_info['lastName'][-2:],
                'Métier': job_info['jobTitle'],
                'Soft-skills': soft_info['softSkills'],
                "Années d'expérience": xp_info['xp'],
                'Savoir-faire clés': savoir_info['SavoirFaireCles'],
                'Compétences techniques': hard_info,
                'Formations': education_info['formation'],
                'Langues': language_info['languages'],
                'Certifications': certification_info['certifications'],
                'Expériences professionnelles': professional_info['professional_experiences'],
                'Projets personnels': personal_info['personal_projects']
            }

            processed_info = preprocess_extracted_info(extracted_info)
            rendered_info = {key: render_item(value) for key, value in processed_info.items()}

            return render(request, 'extractor/result.html', {'rendered_info': rendered_info})
    else:
        form = PDFUploadForm()
    return render(request, 'extractor/upload.html', {'form': form})

@csrf_exempt
def download_doc(request):
    if request.method == 'POST':
        doc_data = request.session.get('doc_data')
        if doc_data:
            response = HttpResponse(doc_data.encode('latin1'), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename="extracted.docx"'
            return response
        return HttpResponse("No document available.")
    return HttpResponse("Invalid request.")
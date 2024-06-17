name_prompt = " identify first name and last name and give me the answer in JSON format{'firstName':'','lastName':''},no explanation give just the JSON"
education_prompt = " identify the high schools,faculties, universities and education and give me the answer in JSON format{'formation':{'school':'','date':'','title':},{'school':'','date':'','title':}...},do not include certifications or short time formation, no explanation give just the JSON"
professional_prompt = """ identify the professional experiences and give me the answer in JSON format{
  "professional_experiences": [
    {
      "job_title": "Job Title",
      "client": "Client",
      "dates": "Dates",
      "context": "Description of the context and the project",
      "achievements": [
        "Achievement 1",
        "Achievement 2",
        "Etc."
      ],
      "challenges_and_solutions": [
        "Example 1",
        "Example 2",
        "Etc."
      ],
      "team_and_methodology": {
        "team": "Team",
        "methodology": "Methodology"
      },
      "technical_environment": "List of tools & technologies used"
    },
    {
      "job_title": "Job Title",
      "client": "Client",
      "dates": "Dates",
      "context": "Description of the context and the project",
      "achievements": [
        "Achievement 1",
        "Achievement 2",
        "Etc."
      ],
      "challenges_and_solutions": [
        "Example 1",
        "Example 2",
        "Etc."
      ],
      "team_and_methodology": {
        "team": "Team",
        "methodology": "Methodology"
      },
      "technical_environment": "List of tools & technologies used"
    },
    {
      "job_title": "Job Title",
      "client": "Client",
      "dates": "Dates",
      "context": "Description of the context and the project",
      "achievements": [
        "Achievement 1",
        "Achievement 2",
        "Etc."
      ],
      "challenges_and_solutions": [
        "Example 1",
        "Example 2",
        "Etc."
      ],
      "team_and_methodology": {
        "team": "Team",
        "methodology": "Methodology"
      },
      "technical_environment": "List of tools & technologies used"
    }
  ]
}, leave empty values you don't find, don't invent new information only extract,no explanation give me just the JSON"""
personal_project_prompt = """ identify the personal projects that were not done inside companies and give me the answer in JSON format{
  {
  "personal_projects": [
    {
      "project_title": "Project Title",
      "dates": "Dates",
      "context": "Description of the context and the project",
      "achievements": [
        "Achievement 1",
        "Achievement 2",
        "Etc."
      ],
      "technical_environment": "List of tools & technologies used"
    },
    {
      "project_title": "Project Title",
      "dates": "Dates",
      "context": "Description of the context and the project",
      "achievements": [
        "Achievement 1",
        "Achievement 2",
        "Etc."
      ],
      "technical_environment": "List of tools & technologies used"
    }
  ]
}, leave empty values you don't find, don't invent new information only extract,no explanation give me just the JSON"""
language_prompt = """ identify the languages and give me the answer in JSON format{
{
  "languages": [
    {
      "language": "Language 1",
      "level": "Level (professional B1, confirmed B2, fluent C1, bilingual C2)"
    },
    {
      "language": "Language 2",
      "level": "Level (professional B1, confirmed B2, fluent C1, bilingual C2)"
    }
  ]
}, leave empty values you don't find,try to convert the levels to professional B1, confirmed B2, fluent C1 or bilingual C2, don't invent new information only extract,no explanation give me just the JSON"""
certification_prompt = """ identify the certifications and give me the answer in JSON format{
{
  "certifications": [
    {
      "certification_name": "Name of the Certification",
      "dates": "Dates"
    },
    {
      "certification_name": "Name of the Certification",
      "dates": "Dates"
    }
  ]
}, leave empty values you don't find, don't invent new information only extract,no explanation give me just the JSON"""
savoir_prompt = """ identify 3 major expertise (savoir-faire) by analyzing the resumé according to the job title and give me the answer in JSON format{
{
  "SavoirFaireCles": [
    "",
    "",
    ""
  ]
  }, don't include expertise of a field different than the job position, be concise and don't invent new information only extract,no explanation give me just the JSON"""
job_prompt = """ identify the job title from the resumé and give me the answer in JSON format{
{
  "jobTitle": ""
  }, don't invent new information only extract,no explanation give me just the JSON"""
soft_prompt = """ identify 3 soft skills from the resumé if mentionned, and give me the answer in JSON format{
{
  "softSkills": [
    "",
    "",
    ""
  ]
  }, leave empty values you don't find, don't invent new information only extract,no explanation give me just the JSON"""
xp_prompt = """ identify the professional experience years relative to the job title domain from the resumé and give me the answer in JSON format{
{
  "xp": ""
  }, calculate only the sum of years of experience relative to the job title field, give only a number don't add the word years, don't invent new information only extract,no explanation give me just the JSON"""
hard_prompt = """ identify all technologies, tools, frameworks ... from the resumé, and give me the answer in JSON format,
{'Langages de programation':['','',...],
'Modélisation':['','',...],	
'Systèmes':['','',...],	
'Plateformes Webservices':['','',...],	
'I.H.M (Librairies graphiques)':['','',...],	
'Serveurs':['','',...],	
'Protocoles & Bus':['','',...],	
'SGBD':['','',...],	
'Gestion de configuration':['','',...],	
'Outils':['','',...],	
'Méthodes':['','',...],
...}	

get inspiration and gudelines for categories from the following JSON
{map_json},
integrate only the keys you find values for,don't include certifications and languages, don't invent new information only extract,no explanation give me just the JSON"""
correction_prompt = """adapt the values of {hard_info} according to {map_json} 
avoid repetition and give me the answer in JSON format, don't invent new information only existing one,no explanation give me just the JSON
"""
map_json = {
    "Langages_de_Programmation": [
        "C#",
        "JavaScript",
        "TypeScript",
        "HTML",
        "CSS",
        "Sass",
        "Python",
        "Java",
        "C",
        "C++",
        "Swift",
        "Kotlin",
        "PHP",
        "Ruby",
        "Rust",
        "Go",
        "SQL",
        "R",
        "MATLAB",
        "Scala",
        "Lua",
        "Objective-C",
        "Perl",
        "Dart",
        "Haskell"
    ],
    "Mod\u00e9lisation": [
        "MLD (Mod\u00e8le Logique de Donn\u00e9es)",
        "MCD (Mod\u00e8le Conceptuel de Donn\u00e9es)",
        "MPD (Mod\u00e8le Physique de Donn\u00e9es)",
        "MVC (Mod\u00e8le-Vue-Contr\u00f4leur)"
    ],
    "Syst\u00e8mes": [
        "Linux",
        "Windows",
        "MacOS",
        "UNIX",
        "FreeBSD",
        "Solaris"
    ],
    "Plateformes_Webservices": [
        "REST",
        "API",
        "Webservices",
        "Swagger",
        "SOAP UI",
        "GraphQL"
    ],
    "IHM (Librairies graphiques)": [
        "Angular",
        "React",
        "Bootstrap",
        "AngularJS",
        "Vue.js",
        "jQuery",
        "Svelte",
        "Ember.js"
    ],
    "Serveurs": [
        "NodeJS",
        "Node Express",
        "Django",
        "Flask",
        "Spring Boot",
        "ASP.NET",
        "Ruby on Rails",
        "Nginx",
        "Apache",
        "Tomcat"
    ],
    "Framework": [
        ".Net",
        ".Net Core",
        "React",
        "Angular",
        "Nunit",
        "Moq",
        "Jest",
        "NodeJS",
        "Node Express",
        "Django",
        "Flask",
        "Spring",
        "Rails"
    ],
    "SGBD (Syst\u00e8mes de Gestion de Base de Donn\u00e9es)": [
        "SQLServer",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "Oracle",
        "SQLite",
        "Redis",
        "Cassandra",
        "MariaDB"
    ],
    "Gestion_de_Configuration": [
        "Git",
        "GitHub",
        "GitLab",
        "Azure DevOps",
        "Bitbucket",
        "Subversion (SVN)",
        "Mercurial"
    ],
    "DevOps / Cloud / IA": [
        "Jenkins",
        "Docker",
        "AWS (Amazon Web Services)",
        "Terraform",
        "Azure",
        "Kubernetes",
        "Google Cloud Platform (GCP)",
        "Ansible",
        "Chef",
        "Puppet"
    ],
    "Outils": [
        "Visual Studio",
        "Visual Studio Code",
        "IntelliJ IDEA",
        "PyCharm",
        "Eclipse",
        "NetBeans",
        "Atom",
        "Sublime Text",
        "Postman"
    ],
    "M\u00e9thodes": [
        "Agile (Scrum)",
        "Kanban",
        "Lean",
        "XP (Extreme Programming)",
        "Waterfall",
        "DevOps",
        "SAFe (Scaled Agile Framework)"
    ],
    "Productivit\u00e9 et Analyse de Donn\u00e9es": [
        "Microsoft Office (Word, Excel, PowerPoint, Outlook)",
        "Power BI",
        "Tableau",
        "Google Workspace (Docs, Sheets, Slides)",
        "Zoho Office Suite",
        "LibreOffice",
        "Apache OpenOffice"
    ],
    "Cybersecurity": {
        "Tools": [
            "Wireshark",
            "Metasploit",
            "Nessus",
            "Nmap",
            "Burp Suite",
            "OpenVAS",
            "Snort",
            "Kali Linux",
            "Aircrack-ng",
            "John the Ripper"
        ],
        "Certifications": [
            "CISSP",
            "CEH",
            "CompTIA Security+",
            "OSCP",
            "GSEC",
            "CISM",
            "CISA",
            "Cisco Certified CyberOps Associate"
        ],
        "Frameworks and Standards": [
            "NIST Cybersecurity Framework",
            "ISO/IEC 27001",
            "COBIT",
            "PCI DSS",
            "GDPR"
        ]
    },
    "Networking": {
        "Protocols": [
            "TCP/IP",
            "HTTP/HTTPS",
            "FTP/SFTP",
            "SMTP",
            "SNMP",
            "BGP",
            "OSPF",
            "MPLS",
            "VLAN",
            "VPN"
        ],
        "Hardware": [
            "Routers",
            "Switches",
            "Firewalls",
            "Access Points",
            "Network Interface Cards (NICs)",
            "Load Balancers"
        ],
        "Certifications": [
            "CCNA",
            "CCNP",
            "CompTIA Network+",
            "JNCIA",
            "CWNP",
            "CCIE"
        ],
        "Tools": [
            "Cisco Packet Tracer",
            "GNS3",
            "SolarWinds Network Performance Monitor",
            "NetFlow Analyzer",
            "Nagios",
            "PRTG Network Monitor"
        ]
    },
    "Cloud Computing": {
        "Platforms": [
            "AWS",
            "Microsoft Azure",
            "Google Cloud Platform (GCP)",
            "IBM Cloud",
            "Oracle Cloud",
            "Alibaba Cloud"
        ],
        "Certifications": [
            "AWS Certified Solutions Architect",
            "Microsoft Certified: Azure Solutions Architect Expert",
            "Google Cloud Professional Cloud Architect",
            "CompTIA Cloud+",
            "CCSP"
        ],
        "Tools": [
            "Terraform",
            "Ansible",
            "Kubernetes",
            "Docker",
            "Jenkins",
            "Prometheus",
            "Grafana"
        ]
    },
    "Data Science and Machine Learning": {
        "Tools_and_Libraries": [
            "Jupyter Notebook",
            "Anaconda",
            "TensorFlow",
            "PyTorch",
            "Scikit-learn",
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Keras",
            "Hugging Face"
        ],
        "Certifications": [
            "Certified Data Scientist (CDS)",
            "CCP Data Engineer",
            "Azure Data Scientist Associate",
            "Google Professional Data Engineer"
        ]
    },
    "Data Engineering": {
        "Tools_and_Technologies": [
            "Apache Hadoop",
            "Apache Spark",
            "Apache Kafka",
            "Apache Flink",
            "Airflow",
            "Tableau",
            "Power BI",
            "Snowflake",
            "AWS Redshift",
            "Google BigQuery",
            "Azure Synapse Analytics",
            "dbt (Data Build Tool)",
            "Informatica",
            "Talend"
        ],
        "Certifications": [
            "Google Professional Data Engineer",
            "AWS Certified Data Analytics - Specialty",
            "Azure Data Engineer Associate",
            "Cloudera Certified Data Engineer"
        ]
    },
    "Project Management": {
        "Methodologies": [
            "Agile",
            "Scrum",
            "Kanban",
            "Waterfall",
            "Lean",
            "PRINCE2"
        ],
        "Certifications": [
            "PMP",
            "CSM",
            "PRINCE2 Practitioner",
            "Certified Agile Project Manager (IAPM)",
            "CompTIA Project+"
        ],
        "Tools": [
            "Jira",
            "Trello",
            "Asana",
            "Microsoft Project",
            "Monday.com",
            "Wrike",
            "Basecamp"
        ]
    }
}
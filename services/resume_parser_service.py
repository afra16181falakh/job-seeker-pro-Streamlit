import requests
import os
from dotenv import load_dotenv
import base64

# Load environment variables from .env file
load_dotenv()

def parse_resume(file_path):
    """Parses a resume file using the RapidAPI resume parsing API.

    Args:
        file_path (str): Path to the resume file.

    Returns:
        dict: Parsed resume data as a JSON object, or None if there was an error.
    """
    rapidapi_key = os.getenv("RAPIDAPI_KEY")  # Get API key from environment variable
    if not rapidapi_key:
        print("Error: RapidAPI key not found in environment variables.")
        return None

    url = "https://resume-parsing-api2.p.rapidapi.com/processDocument"

    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
            base64_file = base64.b64encode(file_content).decode("utf-8")

        payload = {
            "extractionDetails": {
                "name": "Resume - Extraction",
                "language": "English",
                "fields": [
                    {
                        "key": "personal_info",
                        "description": "personal information of the person",
                        "type": "object",
                        "properties": [
                            {
                                "key": "name",
                                "description": "name of the person",
                                "example": "Alex Smith",
                                "type": "string"
                            },
                            {
                                "key": "email",
                                "description": "email of the person",
                                "example": "alex.smith@gmail.com",
                                "type": "string"
                            },
                            {
                                "key": "phone",
                                "description": "phone of the person",
                                "example": "0712 123 123",
                                "type": "string"
                            },
                            {
                                "key": "address",
                                "description": "address of the person",
                                "example": "Bucharest, Romania",
                                "type": "string"
                            }
                        ]
                    },
                    {
                        "key": "work_experience",
                        "description": "work experience of the person",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": [
                                {
                                    "key": "title",
                                    "description": "title of the job",
                                    "example": "Software Engineer",
                                    "type": "string"
                                },
                                {
                                    "key": "start_date",
                                    "description": "start date of the job",
                                    "example": "2022",
                                    "type": "string"
                                },
                                {
                                    "key": "end_date",
                                    "description": "end date of the job",
                                    "example": "2023",
                                    "type": "string"
                                },
                                {
                                    "key": "company",
                                    "description": "company of the job",
                                    "example": "Fastapp Development",
                                    "type": "string"
                                },
                                {
                                    "key": "location",
                                    "description": "location of the job",
                                    "example": "Bucharest, Romania",
                                    "type": "string"
                                },
                                {
                                    "key": "description",
                                    "description": "description of the job",
                                    "example": "Designing and implementing server-side logic to ensure high performance and responsiveness of applications.",
                                    "type": "string"
                                }
                            ]
                        }
                    },
                    {
                        "key": "education",
                        "description": "school education of the person",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": [
                                {
                                    "key": "title",
                                    "description": "title of the education",
                                    "example": "Master of Science in Computer Science",
                                    "type": "string"
                                },
                                {
                                    "key": "start_date",
                                    "description": "start date of the education",
                                    "example": "2022",
                                    "type": "string"
                                },
                                {
                                    "key": "end_date",
                                    "description": "end date of the education",
                                    "example": "2023",
                                    "type": "string"
                                },
                                {
                                    "key": "institute",
                                    "description": "institute of the education",
                                    "example": "Bucharest Academy of Economic Studies",
                                    "type": "string"
                                },
                                {
                                    "key": "location",
                                    "description": "location of the education",
                                    "example": "Bucharest, Romania",
                                    "type": "string"
                                },
                                {
                                    "key": "description",
                                    "description": "description of the education",
                                    "example": "Advanced academic degree focusing on developing a deep understanding of theoretical foundations and practical applications of computer technology.",
                                    "type": "string"
                                }
                            ]
                        }
                    },
                    {
                        "key": "languages",
                        "description": "languages spoken by the person",
                        "type": "array",
                        "items": {
                            "type": "string",
                            "example": "English"
                        }
                    },
                    {
                        "key": "skills",
                        "description": "skills of the person",
                        "type": "array",
                        "items": {
                            "type": "string",
                            "example": "NodeJS"
                        }
                    },
                    {
                        "key": "certificates",
                        "description": "certificates of the person",
                        "type": "array",
                        "items": {
                            "type": "string",
                            "example": "AWS Certified Developer - Associate"
                        }
                    }
                ]
            },
            "file": f"data:application/octet-stream;base64,{base64_file}" #Removed helpers import, included logic here
        }

        headers = {
            "x-rapidapi-key": rapidapi_key,
            "x-rapidapi-host": "resume-parsing-api2.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()  # Return JSON data if successful

    except requests.exceptions.RequestException as e:
        print(f"API Request Failed: {e}")
        return None  # Return None to indicate an error
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"Error encoding file to base64: {e}")
        return None
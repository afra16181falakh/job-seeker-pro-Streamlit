import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

def get_linkedin_company_insights(username):
    """Fetches company insights from LinkedIn using the RapidAPI.

    Args:
        username (str): The LinkedIn username of the company.

    Returns:
        dict: Company insights as a JSON object, or None if there was an error.
    """
    rapidapi_key = os.getenv("RAPIDAPI_KEY")  # Get API key from environment variable
    if not rapidapi_key:
        print("Error: RapidAPI key not found in environment variables.")
        return None

    url = f"https://linkedin-api8.p.rapidapi.com/get-company-insights?username={username}"

    querystring = {"username": username}

    headers = {
        "x-rapidapi-key": rapidapi_key,
        "x-rapidapi-host": "linkedin-api8.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()  # Return JSON data if successful
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None  # Return None to indicate an error


def create_linkedin_job_posting(title, description, location):
    api_endpoint = "https://api.linkedin.com/v2/simpleJobPostings"
    linkedin_access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")  # Replace with your access token from OAuth

    # Replace the sample POST request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {linkedin_access_token}',
    }

    data = {
        "elements": [
            {
                "externalJobPostingId": "external-job-id-0001",
                "title": title,
                "description": description,
                "location": location,
                "integrationContext": "urn:li:organization:1234",
                "listedAt": 1558045934000,
                "jobPostingOperationType": "CREATE",
                "location": "Enterprise, UT",
                "availability": "PUBLIC",
                "industries": [
                    "urn:li:industry:3"
                ],
                "categories": [
                    "advr"
                ],
                "trackingPixelUrl": "http://localhost:5000/jobs/tracking",
                "companyApplyUrl": "http://localhost:5000",
                "posterEmail": "test@email.com",
                "onsiteApplyConfiguration": {
                    "jobApplicationWebhookUrl": "https://customer-webhook.com/api/webhook",
                    "questions": {
                        "voluntarySelfIdentificationQuestions": {},
                        "educationQuestions": {
                            "educationExperienceQuestionSet": {}
                        },
                        "workQuestions": {
                            "workExperienceQuestionSet": {}
                        },
                        "additionalQuestions": {
                            "customQuestionSets": [
                                {
                                    "repeatLimit": 1,
                                    "questions": [
                                        {
                                            "required": True,
                                            "partnerQuestionIdentifier": "question1",
                                            "questionText": "Please choose the right answer",
                                            "questionDetails": {
                                                "multipleChoiceQuestionDetails": {
                                                    "choices": [
                                                        {
                                                            "symbolicName": "wrong",
                                                            "displayValue": "This is the wrong answer"
                                                        },
                                                        {
                                                            "symbolicName": "right",
                                                            "displayValue": "This is the correct answer"
                                                        },
                                                        {
                                                            "symbolicName": "right2",
                                                            "displayValue": "This is also the correct answer"
                                                        }
                                                    ],
                                                    "selectMultiple": False,
                                                    "defaultValueSymbolicName": "right",
                                                    "preferredFormComponent": "DROPDOWN",
                                                    "favorableMultipleChoiceAnswer": {
                                                        "favorableSymbolicNames": [
                                                            "right",
                                                            "right2"
                                                        ]
                                                    }
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
            }
        ]
    }

    try:
        response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Request Failed: {e}")
        return None
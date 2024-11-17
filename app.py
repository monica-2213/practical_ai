# Import necessary libraries
from dotenv import load_dotenv
import os
import requests

# Load environment variables from the .env file
load_dotenv()

# Get credentials from environment variables
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_KEY")

# Example function to call the Azure Vision API (OCR)
def analyze_image(image_url):
    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_KEY,
        'Content-Type': 'application/json'
    }

    params = {
        'language': 'en',
        'detectOrientation': 'true'
    }

    # Form the Azure Vision API request
    body = {
        'url': image_url
    }

    # Send the request to the Azure Vision API
    response = requests.post(f'{AZURE_ENDPOINT}/vision/v3.2/ocr', headers=headers, params=params, json=body)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
image_url = "https://www.simplilearn.com/ice9/free_resources_article_thumb/what_is_Computer_Vision.jpg"
result = analyze_image(image_url)

# Print the OCR result
print(result)

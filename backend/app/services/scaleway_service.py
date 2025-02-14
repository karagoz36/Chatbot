# app/services/scaleway_service.py
import os
import requests
import json
from dotenv import load_dotenv

print("Loading environment variables...")
load_dotenv()

class ScalewayService:
    def __init__(self):
        self.access_key = os.getenv("SCW_ACCESS_KEY")
        self.secret_key = os.getenv("SCW_SECRET_KEY")
        self.mistral = "***REMOVED***"
        self.base_url = "https://api.mistral.ai/v1/chat/completions"

    async def generate_text(self, prompt: str):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Auth-Token": self.secret_key,
            "Authorization": f"Bearer {self.mistral}"
        }

        payload = {
            "model": "mistral-large-latest",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 256,
            "temperature": 0.7
        }

        try:
            print(f"Making request with payload: {json.dumps(payload)}")  # Debug log
            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            print(f"Response status: {response.status_code}")  # Debug log
            print(f"Response body: {response.text}")  # Debug log

            if response.status_code == 200:
                response_data = response.json()
                return response_data['choices'][0]['message']['content']
            else:
                raise Exception(f"Error: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {str(e)}")  # Debug log
            raise Exception(f"Request failed: {str(e)}")
        except Exception as e:
            print(f"General error: {str(e)}")  # Debug log
            raise

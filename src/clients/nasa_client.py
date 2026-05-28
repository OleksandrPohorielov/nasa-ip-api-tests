import os
import requests
from dotenv import load_dotenv


load_dotenv()


class NasaClient:
    def __init__(self):
        self.api_key = os.getenv("NASA_API_KEY")
        self.apod_url = os.getenv("NASA_APOD_URL")

    def get_apod(self, requested_date):
        params = {
            "api_key": self.api_key,
            "date": requested_date
        }

        response = requests.get(self.apod_url, params=params)
        return response
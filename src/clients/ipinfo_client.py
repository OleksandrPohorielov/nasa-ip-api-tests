import os
import requests
from dotenv import load_dotenv


load_dotenv()


class IpInfoClient:
    def __init__(self):
        self.ipinfo_url = os.getenv("IPINFO_IP_URL", "https://ipinfo.io/ip")

    def get_public_ip(self):
        response = requests.get(self.ipinfo_url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
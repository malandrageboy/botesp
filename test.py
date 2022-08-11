import requests
import os
from dotenv import load_dotenv

load_dotenv()

# SERVER = os.getenv("BACKEND")
SERVER = "http://localhost:5000/"
# req = requests.get(SERVER + "message")
# print(req.json())


requests.post(SERVER + "message", json={"message": "oioioioi"})
# requests.post(SERVER + "message?message=oioioi")
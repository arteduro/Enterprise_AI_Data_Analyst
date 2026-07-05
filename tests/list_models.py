"""
tests/list_models.py

Lista todos los modelos disponibles para la API Key actual.
"""

from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("\n===== MODELOS DISPONIBLES =====\n")

for model in client.models.list():
    print(model.name)
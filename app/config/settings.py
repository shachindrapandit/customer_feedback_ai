from dotenv import load_dotenv
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

ENV_PATH = BASE_DIR / "ABC_AZURE.env"

load_dotenv(dotenv_path=ENV_PATH)


class Settings:
    AZURE_ENDPOINT = os.getenv("MODEL_ENDPOINT")
    MODEL_NAME = os.getenv("CHAT_MODEL_NAME")
    API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    API_VERSION = os.getenv("api_version")
from langchain_openai import AzureChatOpenAI
from app.config.settings import Settings


class LLMService:

    @staticmethod
    def get_llm():

        return AzureChatOpenAI(
            azure_deployment=Settings.MODEL_NAME,
            api_version=Settings.API_VERSION,
            azure_endpoint=Settings.AZURE_ENDPOINT,
            api_key=Settings.API_KEY,
            temperature=0
        )
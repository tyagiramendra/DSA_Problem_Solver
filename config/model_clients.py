from autogen_ext.models.openai import OpenAIChatCompletionClient
from config import constants as co

def get_openai_model_client():
    return OpenAIChatCompletionClient(model=co.MODEL_NAME, temperature=co.TEMPERATURE,api_key=co.OPENAI_API_KEY)
from google import genai
from app.config import setting


client = genai.Client(api_key=setting.api_key)


def ask_llm(messages,tools= None):
    return client.models.generate_content(
        model=setting.model,
        contents=messages
    )



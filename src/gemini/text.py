from src.gemini.agent import client
from src.config import DEFAULT_MODEL_TEXT, DEFAULT_THINKING
from src.models.base import Carrossel

from google.genai import types

def get_from_gemini_text(
    input_message: str,
    sys_instructs:str,
    response_model=Carrossel,
    model=DEFAULT_MODEL_TEXT
    ):
    response = client.models.generate_content(
        model=model,
        contents=input_message,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=DEFAULT_THINKING),
            system_instruction=sys_instructs,
            response_mime_type="application/json",
            response_schema=response_model
        )
    )

    converted: response_model = response.parsed

    return converted

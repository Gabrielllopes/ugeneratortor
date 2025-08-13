from src.gemini.agent import client
from src.config import DEFAULT_MODEL_IMAGE, DEFAULT_N_IMAGES, DEFAULT_ASPECT_RATIO

from google.genai import types

def get_from_gemini_image(
        input_messge: str,
        model=DEFAULT_MODEL_IMAGE,
        n_image=DEFAULT_N_IMAGES,
        aspect_ratio=DEFAULT_ASPECT_RATIO
    ):
    response = client.models.generate_images(
        model=model,
        prompt=input_messge,
        config=types.GenerateImagesConfig(
            number_of_images=n_image,
            aspectRatio=aspect_ratio
        )
    )
    return response
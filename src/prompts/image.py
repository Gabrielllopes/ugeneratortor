from src.models.base import Language

def generate_ilustration(style: str, language: Language):
    return f"""
        Create an illustration in the style of {style}.
        The text must be written in {language} and seamlessly integrated into the body of the image, ensuring it is clear and visually appealing.
        Include the following text exactly as provided:
    """
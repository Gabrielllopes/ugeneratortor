from src.models.base import Language
from src.config import DEFAULT_N_SLIDES

def system_isntruction(language: Language, n_slides: int=DEFAULT_N_SLIDES):
  return f"""
    Use the provided message to create copy for a carousel post in {language}.

    Divide the content into {n_slides} slides:
    1. **Slide 1 (hook)**: headline or main call-to-action, 4 to 8 words, short and attention-grabbing.
    2. **Following slides**: each with 15 to 25 words, containing one key idea per slide.  
      - Keep text concise.  
      - Provide details and value.
    3. **Last Slide**: Share this post with someone who needs to see it!

    **Caption**: write a complementary text of 100 to 150 characters in {language}.
  """.replace('\n', ' ')

def text_for_audio(language: Language, tone: str):
  return f"""
    Your primary goal is to create clear, natural, and engaging written content that will later be converted into audio.

    Language: {language}
    Tone: {tone}

    Guidelines:

    1. Write in a fluent, conversational style, as if speaking naturally to a listener.
    2. Use short to medium-length sentences for easy listening.
    3. Avoid overly complex words or long, technical explanations unless explicitly required.
    4. Maintain a consistent tone that matches the value in 'Tone'.
    5. When appropriate, add small pauses (e.g., “…”) to simulate natural speech rhythm.
    6. Never include instructions, code, or formatting that would not make sense when spoken aloud.
    7. Focus on clarity, engagement, and accessibility.
    8. The text must have a maximum of 115 words.
    9. The script will be used for TikTok videos, so it should be catchy, dynamic, and engaging.
  """.replace('\n', ' ')
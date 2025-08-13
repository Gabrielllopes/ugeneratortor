from src.models.base import Language

def system_isntruction(language: Language, n_slides: int):
  return f"""
    Use the provided message to create copy for a carousel post in {language}.

    Divide the content into {n_slides} slides:
    1. **Slide 1 (hook)**: headline or main call-to-action, 4 to 8 words, short and attention-grabbing.
    2. **Following slides**: each with 15 to 25 words, containing one key idea per slide.  
      - Keep text concise.  
      - Provide details and value.
    3. **Last Slide**: Share this post with someone who needs to see it!

    **Caption**: write a complementary text of 100 to 150 characters in {language}.
  """
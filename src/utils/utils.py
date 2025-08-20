from src.models.base import ILUSTRATIONS_STYLE, TONE_STYLE, GOOGLE_VOICE_OPTIONS

def get_ilustration_styles():
    print("\n".join(f"{k} - {v}" for k, v in ILUSTRATIONS_STYLE.items()))

def get_tone_styles():
    print("\n".join(f"{k} - {v}" for k, v in TONE_STYLE.items()))

def get_google_voices():
    print("\n".join(f"{k} - {v}" for k, v in GOOGLE_VOICE_OPTIONS.items()))
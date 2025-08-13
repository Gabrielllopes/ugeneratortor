from src.models.base import ILUSTRATIONS_STYLE

def get_ilustration_styles():
    print("\n".join(f"{k}: {v}" for k, v in ILUSTRATIONS_STYLE.items()))
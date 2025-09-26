def generate_prompt_video(script: str):
    return f"""
        Generate a short video that is visually shocking and intense, inspired only by the central theme of the provided script.
        The video should not literally follow the script or illustrate specific lines.
        Instead, create powerful, surreal, and contrasting imagery that conveys emotion and visual impact.
        Use quick cuts, abrupt perspective shifts, and strong contrasts of color and light to amplify the sense of shock.
        The script is only a thematic reference — the video must be autonomous and evocative, working even without narration.

        script {script}
    """


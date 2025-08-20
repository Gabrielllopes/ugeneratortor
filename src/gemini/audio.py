from src.gemini.agent import client

from google.genai import types

def text_to_speach(
    input_message: str,
    voice_name:str,
    model="gemini-2.5-flash-preview-tts"
    ):
    response = client.models.generate_content(
        model=model,
        contents=input_message,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name=voice_name,
                    )
                )
            ),
        )
    )

    return response.candidates[0].content.parts[0].inline_data.data

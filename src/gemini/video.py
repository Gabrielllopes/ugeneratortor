from src.gemini.agent import client

from google.genai import types

import time

def generate_video(prompt, model, save_path, file_name, negative_prompt=None, aspect_ratio=None, base_image=None):

    operation = client.models.generate_videos(
        model=model,
        prompt=prompt,
        image=base_image,
        config=types.GenerateVideosConfig(negative_prompt=negative_prompt, aspectRatio=aspect_ratio),
    )
    # Poll the operation status until the video is ready.
    while not operation.done:
        print("Waiting for video generation to complete...")
        time.sleep(5)
        operation = client.operations.get(operation)
        
    generated_video = operation.response.generated_videos[0]
    client.files.download(file=generated_video.video)
    generated_video.video.save(f"{save_path}/{file_name}")

    return generated_video
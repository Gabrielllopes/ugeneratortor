# AI Content Generation Project

This project aims to automate the creation of **short videos, audio
narrations, and carousel posts** using AI.\
The user simply selects a theme, and the system generates the content
automatically.

The infrastructure is built on **Google Cloud Platform (GCP)** using
**Gemini**, chosen because Google provides free credits for testing.

------------------------------------------------------------------------

## 📒 Notebooks

To simplify the usage of implemented libraries and automate the
pipeline, this folder contains Jupyter notebooks:

### `gemini_api`

Notebook for basic tests and interactions with the Gemini API.

### `image_post_generator`

Notebook to automatically generate carousel-style posts.

**Workflow:** - User defines the theme.\
- Chooses the illustration style.\
- Specifies the number of images.\
- Selects the post language.

The pipeline uses Gemini text generation (with system prompts) to create
a structured schema. Then, Gemini image generation is used to create
each slide.

Since some images may be of low quality, the system generates multiple
variations per input, allowing the user to choose the best final result.

### `video_generator`

Notebook to automatically generate short videos.

**Workflow:** - User defines the theme, language, and narration tone.\
- Gemini text generation creates the script, title, and captions.\
- Gemini audio generates narration in `.mp4` format.\
- Gemini video generates a short video.

Due to video length limitations, the video is looped until the audio
finishes.\
A custom Python video editor was implemented to merge and sync audio and
video.

### `explore`

Contains a notebook for interacting with the **Instagram API**,
assisting in automated carousel post publishing.

------------------------------------------------------------------------

## 📂 Source Code (`src`)

Custom library for project implementation:

-   **`editor`**: Python video editor, responsible for merging
    audio/video and applying edits.\
-   **`gemini`**: Abstractions and wrappers for Gemini API calls.\
-   **`models`**: Data models.\
-   **`grompts`**: Prompt bases and system instructions.\
-   **`utils`**: Helper functions for audio, video, image manipulation,
    and general Python utilities.

------------------------------------------------------------------------

## ☁️ Infrastructure (`terraform`)

Terraform is used to provision the only required cloud service:\
- A GCP bucket to store images before publishing to Instagram.

> If you do not plan to use the Instagram publishing API, you can
> disregard the Terraform setup.

------------------------------------------------------------------------

## 🚀 Summary

This project provides a **fully automated AI pipeline** for content
creation:\
- Carousel posts (text + images)\
- Short videos (script + narration + video loop)\
- Automated publishing support (Instagram integration)

Built with **GCP** and **Gemini**, it allows scalable, AI-driven content
creation with minimal user input.

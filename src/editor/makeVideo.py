from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips


def merge_audio_video(video_files, audio_files, output_file):
    # Carrega e concatena vídeos
    video_clips = [VideoFileClip(f) for f in video_files]
    video = concatenate_videoclips(video_clips, method="chain")  # Garante VideoFileClip
    video_duration = video.duration

    # Carrega e concatena áudios
    audio_clips = [AudioFileClip(f) for f in audio_files]
    audio = concatenate_audioclips(audio_clips)
    audio_duration = audio.duration

    # # Ajusta duração
    # if audio_duration > video_duration:
    #     n_loops = int(audio_duration // video_duration) + 1
    #     video_loop = concatenate_videoclips([video] * n_loops, method="chain")
    #     video_final = video_loop.subclip(0, audio_duration)
    # else:
    #     video_final = video.subclip(0, audio_duration)

    final = video.set_audio(audio)
    final.write_videofile(output_file, codec="libx264", audio_codec="aac")
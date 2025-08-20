import wave
from pydub import AudioSegment


def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)


def mp4_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    audio = AudioSegment(
        data=pcm,
        sample_width=sample_width,
        frame_rate=rate,
        channels=channels
    )
    audio.export(filename, format="mp4")
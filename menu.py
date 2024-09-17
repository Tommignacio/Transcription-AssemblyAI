# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "7084158d63ef470a9a622858ca9f62e0"
config = aai.TranscriptionConfig(language_code="es")
transcriber = aai.Transcriber(config=config)

# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
transcript = transcriber.transcribe("2.mp4")

if transcript.error:
   print(transcript.error)

print(transcript.text)

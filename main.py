from google.cloud import texttospeech
from pypdf import PdfReader


client = texttospeech.TextToSpeechClient()
reader = PdfReader('Text To Audio/Testpdf.pdf')
page = reader.pages[0]
parts = [page.extract_text().replace("\n", ' ')]

synthesis_input = texttospeech.SynthesisInput(text=parts[0])

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("Final Audio/Output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "Output.mp3"')

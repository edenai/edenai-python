# Text-to-speech (TTS) system converts natural written text into an audio speech.

# pip install edenai

host="http://api.edenai.run/"

from edenai import Audio

# Get your API key here: https://app.edenai.run/admin/account
audio_apis = Audio(Your_API_key)

result = audio_apis.text_to_speech(
# Available providers and languages here: https://api.edenai.run/v1/redoc/#operation/Text%20To%20Speech
    text="Your text",
    option="FEMALE",
    providers=["microsoft","google"],
    language="en-US")

print(result)

from IPython.display import Audio
Audio(url=host+result['Microsoft Azure']['audio_path'])
Audio(url=host+result['Google Cloud']['audio_path'])

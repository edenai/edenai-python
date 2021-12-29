# Speech-to-Text (or speech recognition) is technology that can recognize spoken words, which can then be converted to text.

# pip install edenai

from edenai import Audio

# Get your API key here: https://app.edenai.run/admin/account
audio_apis = Audio("Your_API_key")

result = audio_apis.speech_to_text(
# Available providers and languages here: https://api.edenai.run/v1/redoc/#operation/Speech%20Recognition
    file="your_audio.wav",
    providers=["amazon", "ibm"],
    language="en-US")

print(result) 

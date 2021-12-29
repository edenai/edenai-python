# Language Detection or language guessing is the algorithm of determining which natural language given content is in.

# pip install edenai

from edenai import Translation

# Get your API key here: https://app.edenai.run/admin/account
translation_apis = Translation("Your_API_key")

result = translation_apis.language_detection(
# Available providers and languages here: https://api.edenai.run/v1/redoc/#operation/Language%20Detection
   text="Your text written in an unknown language",
   providers=["amazon", "ibm"])

print(result) 

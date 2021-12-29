# Machine translation (or automatic translation) refers to the translation of a text into another language.

# pip install edenai

from edenai import Translation

# Get your API key here: https://app.edenai.run/admin/account
translation_apis = Translation("Your_API_key")

result = translation_apis.translation(
# Available providers and languages here: https://api.edenai.run/v1/redoc/#operation/Automatic%20Translation
   text_to_translate= "The text you want to translate",
   providers=["amazon", "ibm"],
   source_language="en-US",
   target_language="fr-FR")

print(result) 

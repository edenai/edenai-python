# Keyword extraction consists of automatically extracting the most important words and expressions in a text.

# pip install edenai

from edenai import Text

# Get your API key here: https://app.edenai.run/admin/account
text_apis = Text("Your_API_key")

result = text_apis.keyword_extraction(
# Available providers and languages here: https://api.edenai.run/v1/redoc/#operation/Keyword%20Extraction
    text="Your text",
    providers=["amazon", "ibm"],
    language="en-US")

print(result) 

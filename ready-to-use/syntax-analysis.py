# Syntax analysis consists principaly in highlighting the structure of a text.

# pip install edenai

from edenai import Text

# Get your API key here: https://app.edenai.run/admin/account
text_apis = Text("Your_API_key")

result = text_apis.syntax_analysis(
# Available providers and languages here: https://api.edenai.run/v1/redoc/#operation/Syntax%20Analysis
    text="Your text",
    providers=["lettria", "microsoft"],
    language="en-US")

print(result) 

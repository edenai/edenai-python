# Sentiment analysis extracts sentiment in a given string of text. Sentiment analysis, also called 'opinion mining', uses natural language processing, text analysis and computational linguistics to identify and detect subjective information from the input text.

# pip install edenai

from edenai import Text

# Get your API key here: https://app.edenai.run/admin/account
text_apis = Text("Your_API_key")

result = text_apis.sentiment_analysis(
# Available providers and languages here: https://api.edenai.run/v1/redoc/#operation/Sentiment%20Analysis
    text="Your text",
    providers=["amazon", "ibm"],
    language="en-US")

print(result) 

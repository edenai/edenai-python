# Explicit content detection is a computer vision technology which allows to detect explicit content on images: violence, pornography, etc. 

# pip install edenai

from edenai import Vision

# Get your API key here: https://app.edenai.run/admin/account
vision_apis = Vision("Your_API_key")

result = vision_apis.explicit_content_detection(
# Available providers, languages and formats here: https://api.edenai.run/v1/redoc/#operation/Explicit%20Content%20Detection
   providers=["google","amazon"],
   file="your_image.png")

print(result) 

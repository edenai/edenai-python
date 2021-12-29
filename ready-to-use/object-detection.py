# Object detection is a computer vision technology which allows to detect common objects on images. 

# pip install edenai

from edenai import Vision

# Get your API key here: https://app.edenai.run/admin/account
vision_apis = Vision("Your_API_key")

result = vision_apis.object_detection(
# Available providers, languages and formats here: https://api.edenai.run/v1/redoc/#operation/Object%20Detection
   providers=["google","amazon"],
   file="your_image.png")

print(result) 

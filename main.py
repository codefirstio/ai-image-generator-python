import os
import openai  # pip install openai
import urllib.request
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

user_prompt = input("Write your prompt for DALL-E 2: ")

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)


file_name = "image" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"
urllib.request.urlretrieve(image_url, file_name)

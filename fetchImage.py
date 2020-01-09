import requests
import sys
import os
import io

# api key for https://unsplash.com/
api_key = os.getenv("API_KEY")

# ids for photo collections on https://unsplash.com/
collection_ids = ["9241034", "256443", "9003041", "8472480"]

response = requests.get(
    "https://api.unsplash.com/photos/random/?collections=" + ",".join(collection_ids) + "&client_id=" + api_key).json()
image = requests.get(response["urls"]["full"])
imageBytes = image.content


f = open("image.jpg", "wb")
f.write(imageBytes)
f.close()

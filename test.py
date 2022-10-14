
import requests
# Init
response = requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=7a7c94979e8f4ad0a6d8c1848a7052e7")
print(response.json())

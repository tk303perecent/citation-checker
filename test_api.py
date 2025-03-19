import requests

url = "http://127.0.0.1:5000/extract"
data = {"text": "Roe v. Wade, 410 U.S. 113 (1973)"}

response = requests.post(url, json=data)
print(response.json())

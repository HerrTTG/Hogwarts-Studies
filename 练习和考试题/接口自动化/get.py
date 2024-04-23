import requests

url = "https://petstore.swagger.io/v2/pet/findByStatus?"

payload = {}
headers = {}

response = requests.request("GET", url, params='status=available', headers=headers, data=payload)
response.raise_for_status()

print(response.json())

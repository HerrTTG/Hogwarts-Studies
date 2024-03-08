import requests

url = "https://petstore.swagger.io/v2/pet/" + '3141943573'

payload = {}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

response.raise_for_status()
print(response.url)

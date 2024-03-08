import json
import requests

url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
    "id": 3141943573,
    "category": {
        "id": 1,
        "name": "cute"
    },
    "name": "Kat",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 5,
            "name": "cute"
        }
    ],
    "status": "sold"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

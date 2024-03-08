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
    "status": "available"
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())

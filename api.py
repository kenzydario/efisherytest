import requests
import json

# Constants for the API base URL and status
BASE_URL = "https://petstore.swagger.io/v2"
STATUS = "available"

def add_new_pet():
    url = f"{BASE_URL}/pet"

    payload = {
        "id": 12345,
        "category": {
            "id": 1,
            "name": "Test Category"
        },
        "name": "Test Pet",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print("Response status code for adding new pet:", response.status_code)
    print("Response content:", response.json())

def update_existing_pet():
    url = f"{BASE_URL}/pet"

    # Modify the payload to update an existing pet
    payload = {
        "id": 12345,
        "category": {
            "id": 1,
            "name": "Updated Category"
        },
        "name": "Updated Pet",
        "photoUrls": [
            "updated_url"
        ],
        "tags": [
            {
                "id": 0,
                "name": "updated_tag"
            }
        ],
        "status": "sold"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.put(url, headers=headers, data=json.dumps(payload))

    print("Response status code for updating existing pet:", response.status_code)
    print("Response content:", response.json())

def retrieve_pets_by_status():
    url = f"{BASE_URL}/pet/findByStatus?status={STATUS}"

    response = requests.get(url)

    print("Response status code for retrieving pets by status:", response.status_code)
    print("Response content:", response.json())

# Run the functions
add_new_pet()
update_existing_pet()
retrieve_pets_by_status()

import requests
import json

# Define the API endpoint
url = "http://localhost:8000/math"

# Create the payload (data) to send in the POST request
payload = {
    "num1": 10,
    "num2": 5,
    "operation": "add"
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response from the server
print(response.json())

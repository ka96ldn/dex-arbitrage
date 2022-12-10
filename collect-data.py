import json
import requests

# Replace these values with your own API keys and information
API_KEY = "YOUR-API-KEY"
API_SECRET = "YOUR-API-SECRET"
EXCHANGE_URL = "https://uniswap.com/v2"

# Set the endpoint and parameters for the API request
endpoint = "/ticker"
params = {
    "symbol": "ETH-USDT"
}

# Add the API key and signature to the request headers
headers = {
    "X-API-KEY": API_KEY,
    "X-API-SIGNATURE": generate_signature(API_SECRET, endpoint, params)
}

# Make the API request
response = requests.get(EXCHANGE_URL + endpoint, params=params, headers=headers)

# Parse the response
data = json.loads(response.text)

# Print the data to the console
print(data)

import json
import requests

# Replace these values with your own API keys and information
API_KEY = "YOUR-API-KEY"
API_SECRET = "YOUR-API-SECRET"
EXCHANGE_URL = "https://api.your-exchange.com/v1"

# Load the data from the JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Find the exchanges with the highest and lowest prices
highest_price_exchange = None
highest_price = 0
lowest_price_exchange = None
lowest_price = float("inf")
for exchange_data in data:
    average_price = exchange_data["average_price"]
    if average_price > highest_price:
        highest_price_exchange = exchange_data["exchange"]
        highest_price = average_price
    if average_price < lowest_price:
        lowest_price_exchange = exchange_data["exchange"]
        lowest_price = average_price

# Calculate the arbitrage profit
profit = highest_price - lowest_price

# Check if the profit is high enough to make a trade
if profit > 0.01:  # 1% profit
    # Set the endpoint and parameters for the buy and sell orders
    buy_endpoint = "/orders"
    buy_params = {
        "symbol": "ETH-USDT",
        "side": "buy",
        "type": "limit",
        "price": lowest_price,
        "quantity": 1
    }
    sell_endpoint = "/orders"
    sell_params = {
        "symbol": "ETH-USDT",
        "side": "sell",
        "type": "limit",
        "price": highest_price,
        "quantity": 1
    }

    # Add the API key and signature to the request headers
    headers = {
        "X-API-KEY": API_KEY,
        "X-API-SIGNATURE": generate_signature(API_SECRET, buy_endpoint, buy_params)
    }

    # Make the API request to buy ETH on the lowest-priced exchange
    response = requests.post(EXCHANGE_URL + buy_endpoint, json=buy_params, headers=headers)
    if response.status_code != 200:
        print("Error placing buy order")
        exit()

    # Make the API request to sell ETH on the highest-priced exchange
    headers["X-API-SIGNATURE"] = generate_signature(API_SECRET, sell_endpoint, sell_params)
    response = requests.post(EXCHANGE_URL + sell_endpoint, json=sell_params, headers=headers)
    if response.status_code != 200:
        print("Error placing sell order")
        exit()

    print("Arbitrage trade completed successfully")
else:
    print("Profit is too low to make a trade")

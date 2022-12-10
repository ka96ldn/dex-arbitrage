import json

# Load the data from the JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Loop through the data and calculate the average price for each exchange
for exchange_data in data:
    total_price = 0
    for ticker in exchange_data["tickers"]:
        total_price += ticker["price"]
    average_price = total_price / len(exchange_data["tickers"])
    print(f"Average price on {exchange_data['exchange']}: {average_price}")

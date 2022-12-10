import requests

class Exchange:
    def __init__(self, api_key, api_secret, base_url):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def _generate_signature(self, endpoint, params):
        """Generate a signature for the API request"""
        # Your implementation goes here

    def _make_request(self, method, endpoint, params):
        """Make an API request to the exchange"""
        url = self.base_url + endpoint
        headers = {
            "X-API-KEY": self.api_key,
            "X-API-SIGNATURE": self._generate_signature(endpoint, params)
        }
        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=params, headers=headers)
        else:
            raise ValueError("Invalid request method")
        return response

    def get_ticker(self, symbol):
        """Get the latest ticker information for a symbol"""
        endpoint = "/ticker"
        params = {
            "symbol": symbol
        }
        response = self._make_request("GET", endpoint, params)
        data = response.json()
        return data

    def place_order(self, symbol, side, order_type, price, quantity):
        """Place an order on the exchange"""
        endpoint = "/orders"
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "price": price,
            "quantity": quantity
        }
        response = self._make_request("POST", endpoint, params)
        return response.status_code == 200

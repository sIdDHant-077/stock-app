from flask import Flask, request, jsonify
import requests

app = Flask("stockdata")

# Stock Data API Endpoint and API Token
STOCK_API_URL = "https://api.stockdata.org/v1/data/quote"
API_TOKEN = "Z01QtrQWMxZyy66Qjm4lMhyKsz4ggm8fkvai89tt"  # Replace with your actual API token
DEFAULT_SYMBOL = "AAPL"

@app.route('/get-stock', methods=['GET'])
def get_stock():
    """Fetch the most recent stock data for the given symbol."""
    # Get stock symbol from query parameters or use default
    symbol = request.args.get('symbol', DEFAULT_SYMBOL).upper()

    if not symbol:
        return jsonify({"error": "Stock symbol is required!"}), 400

    # Set headers and parameters for the API request
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    params = {"symbols": symbol}

    try:
        # Make the API request to fetch stock data
        response = requests.get(STOCK_API_URL, headers=headers, params=params)

        # Handle successful response
        if response.status_code == 200:
            data = response.json()

            # Check if data is available
            if data.get('data'):
                stock_info = data['data'][0]  # Assuming the most recent data is the first one
                return jsonify(stock_info), 200
            else:
                return jsonify({"error": "No data found for the given symbol!"}), 404

        # Handle errors from the API
        else:
            return jsonify({
                "error": "Failed to fetch stock data.",
                "details": response.json()
            }), response.status_code

    except Exception as e:
        # Handle unexpected exceptions
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
import os
import json
import urllib.request
import urllib.parse

print("=== SMARTFLOW LIVE MARKET DATA ===\n")

# API configuration
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

if not API_KEY:
    print("API key missing!")
    print("Set your API key before running.")
    exit()

# Market settings
from_currency = "EUR"
to_currency = "USD"
interval = "5min"

# API request
params = {
    "function": "FX_INTRADAY",
    "from_symbol": from_currency,
    "to_symbol": to_currency,
    "interval": interval,
    "outputsize": "compact",
    "apikey": API_KEY
}

url = (
    "https://www.alphavantage.co/query?"
    + urllib.parse.urlencode(params)
)

try:
    with urllib.request.urlopen(url, timeout=20) as response:
        data = json.loads(response.read().decode())

    # Check for API errors
    if "Error Message" in data:
        print(data["Error Message"])

    elif "Information" in data:
        print("API Information:", data["Information"])

    elif "Note" in data:
        print("API Limit:", data["Note"])

    else:
        series_key = "Time Series FX (5min)"

        if series_key not in data:
            print("Market data unavailable.")
            print(data)
            exit()

        candles = data[series_key]

        print("Market:", from_currency + "/" + to_currency)
        print("Timeframe:", interval)

        print("\n=== LATEST MARKET CANDLES ===")

        for timestamp, candle in sorted(
            candles.items(),
            reverse=True
        )[:10]:

            print("\nTime:", timestamp)
            print("Open:", candle["1. open"])
            print("High:", candle["2. high"])
            print("Low:", candle["3. low"])
            print("Close:", candle["4. close"])

except Exception as error:
    print("Connection error:", error)

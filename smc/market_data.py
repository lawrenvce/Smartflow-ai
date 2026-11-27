import yfinance as yf

MARKETS = {
    "XAUUSD": "GC=F",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "USDJPY": "JPY=X"
}

def get_market_data(symbol, period="5d", interval="1h"):

    data = yf.download(
        symbol,
        period=period,
        interval=interval,
        progress=False
    )

    return data

if __name__ == "__main__":

    for market, symbol in MARKETS.items():

        print(f"\nScanning {market}...")

        data = get_market_data(symbol)

        print(data.tail())

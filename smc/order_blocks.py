
candles = [
    {"open": 100, "close": 105},
    {"open": 105, "close": 110},
    {"open": 110, "close": 106},
    {"open": 106, "close": 103},
    {"open": 103, "close": 115},
    {"open": 115, "close": 120}
]

print("=== SMARTFLOW ORDER BLOCK DETECTOR ===\n")

for i in range(1, len(candles)):

    previous_candle = candles[i - 1]
    current_candle = candles[i]

    # Bullish Order Block
    if (
        previous_candle["close"] < previous_candle["open"]
        and current_candle["close"] > current_candle["open"]
        and current_candle["close"] > previous_candle["open"]
    ):
        print("Potential Bullish Order Block Detected!")

        print(
            "Order Block Zone:",
            previous_candle["close"],
            "-",
            previous_candle["open"]
        )

    # Bearish Order Block
    elif (
        previous_candle["close"] > previous_candle["open"]
        and current_candle["close"] < current_candle["open"]
        and current_candle["close"] < previous_candle["open"]
    ):
        print("Potential Bearish Order Block Detected!")

        print(
            "Order Block Zone:",
            previous_candle["open"],
            "-",
            previous_candle["close"]
        )

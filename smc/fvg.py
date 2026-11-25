candles = [
    {"high": 100, "low": 95},
    {"high": 110, "low": 101},
    {"high": 115, "low": 105}
]

print("=== SMARTFLOW FVG DETECTOR ===\n")

first_high = candles[0]["high"]
third_low = candles[2]["low"]

if third_low > first_high:

    print("Bullish Fair Value Gap Detected!")

    print(f"Gap Range: {first_high} - {third_low}")

else:
    print("No FVG Detected")

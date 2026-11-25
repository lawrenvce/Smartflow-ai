prices = [100, 105, 102, 110, 107, 120, 115, 125]

print("=== SMARTFLOW BOS DETECTOR ===\n")

swing_highs = []
swing_lows = []

for i in range(1, len(prices) - 1):

    if prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:
        swing_highs.append(prices[i])

    elif prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:
        swing_lows.append(prices[i])

print("Swing Highs:", swing_highs)
print("Swing Lows:", swing_lows)

print("\n=== BOS Detection ===")

latest_price = prices[-1]

if swing_highs:

    last_high = swing_highs[-1]

    if latest_price > last_high:

        print(
            f"Bullish BOS Detected! "
            f"Price {latest_price} broke above {last_high}"
        )

if swing_lows:

    last_low = swing_lows[-1]

    if latest_price < last_low:

        print(
            f"Bearish BOS Detected! "
            f"Price {latest_price} broke below {last_low}"
        )

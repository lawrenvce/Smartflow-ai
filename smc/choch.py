prices = [100, 105, 102, 110, 107, 115, 108, 103]

print("=== SMARTFLOW CHOCH DETECTOR ===\n")

swing_highs = []
swing_lows = []

for i in range(1, len(prices) - 1):

    if prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:
        swing_highs.append(prices[i])

    elif prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:
        swing_lows.append(prices[i])

print("Swing Highs:", swing_highs)
print("Swing Lows:", swing_lows)

print("\n=== CHOCH Detection ===")

latest_price = prices[-1]

if len(swing_lows) >= 1:

    last_low = swing_lows[-1]

    if latest_price < last_low:
        print(
            f"Bearish CHOCH Detected! "
            f"Price {latest_price} broke below {last_low}"
        )
    else:
        print("No CHOCH detected.")

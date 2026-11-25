prices = [100, 105, 102, 110, 107, 115, 111, 120, 118]

print("=== SMARTFLOW MARKET STRUCTURE ===\n")

swing_highs = []
swing_lows = []

for i in range(1, len(prices) - 1):

    prev_price = prices[i - 1]
    current_price = prices[i]
    next_price = prices[i + 1]

    if current_price > prev_price and current_price > next_price:
        swing_highs.append(current_price)

    elif current_price < prev_price and current_price < next_price:
        swing_lows.append(current_price)

print("Swing Highs:", swing_highs)
print("Swing Lows:", swing_lows)

print("\n=== Trend Analysis ===")

# Higher Highs
for i in range(1, len(swing_highs)):
    if swing_highs[i] > swing_highs[i - 1]:
        print(f"Higher High: {swing_highs[i]}")

# Higher Lows
for i in range(1, len(swing_lows)):
    if swing_lows[i] > swing_lows[i - 1]:
        print(f"Higher Low: {swing_lows[i]}")

# Lower Highs
for i in range(1, len(swing_highs)):
    if swing_highs[i] < swing_highs[i - 1]:
        print(f"Lower High: {swing_highs[i]}")

# Lower Lows
for i in range(1, len(swing_lows)):
    if swing_lows[i] < swing_lows[i - 1]:
        print(f"Lower Low: {swing_lows[i]}")

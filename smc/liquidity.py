prices = [100, 105, 110, 108, 115, 120, 123, 118]

print("=== SMARTFLOW LIQUIDITY SWEEP ===\n")

previous_high = max(prices[:-2])

sweep_price = prices[-2]
current_price = prices[-1]

print("Previous High:", previous_high)
print("Sweep Price:", sweep_price)
print("Current Price:", current_price)

if sweep_price > previous_high and current_price < sweep_price:
    print("\nLiquidity Sweep Detected!")
else:
    print("\nNo Liquidity Sweep")


print("=== SMARTFLOW SIGNAL GENERATOR ===\n")

# Bullish conditions
bullish_bos = True
bullish_sweep = True
bullish_fvg = True
bullish_order_block = True

# Bearish conditions
bearish_bos = False
bearish_sweep = False
bearish_fvg = False
bearish_order_block = False

# BUY SIGNAL
if (
    bullish_bos
    and bullish_sweep
    and bullish_fvg
    and bullish_order_block
):
    print("BUY SIGNAL")
    direction = "BUY"

# SELL SIGNAL
elif (
    bearish_bos
    and bearish_sweep
    and bearish_fvg
    and bearish_order_block
):
    print("SELL SIGNAL")
    direction = "SELL"

else:
    print("NO TRADE")
    direction = "NONE"

print("\nTrade Direction:", direction)

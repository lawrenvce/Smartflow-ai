from smc.multi_timeframe import analyze_timeframes

print("================================")
print("      SMARTFLOW AI ENGINE")
print("================================\n")

signal = analyze_timeframes(
    htf_trend="bullish",
    mtf_trend="bullish",
    ltf_signal="bullish"
)

print(f"\nTrade Signal: {signal}")

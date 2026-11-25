def analyze_timeframes(htf_trend, mtf_trend, ltf_signal):

    if (
        htf_trend == "bullish"
        and mtf_trend == "bullish"
        and ltf_signal == "bullish"
    ):
        return "BUY"

    elif (
        htf_trend == "bearish"
        and mtf_trend == "bearish"
        and ltf_signal == "bearish"
    ):
        return "SELL"

    else:
        return "NO TRADE"


if __name__ == "__main__":

    signal = analyze_timeframes(
        "bullish",
        "bullish",
        "bullish"
    )

    print(signal)

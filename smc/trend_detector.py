def detect_trend(closes):

    if len(closes) < 20:
        return "insufficient data"

    if closes.iloc[-1] > closes.iloc[-20]:
        return "bullish"

    elif closes.iloc[-1] < closes.iloc[-20]:
        return "bearish"

    return "neutral"

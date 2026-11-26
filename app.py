import streamlit as st

from smc.multi_timeframe import analyze_timeframes

st.set_page_config(
    page_title="SmartFlow AI",
    layout="wide"
)

st.title("📈 SmartFlow AI Dashboard")

signal = analyze_timeframes(
    htf_trend="bullish",
    mtf_trend="bullish",
    ltf_signal="bullish"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("4H Trend", "Bullish")

with col2:
    st.metric("1H Trend", "Bullish")

with col3:
    st.metric("15M Entry", "Bullish")

with col4:
    st.metric("Signal", signal)

st.divider()

st.subheader("Risk Settings")

account_balance = 10000
risk_percent = 1

st.write(f"Account Balance: ${account_balance}")
st.write(f"Risk Per Trade: {risk_percent}%")

if signal == "BUY":
    st.success("✅ BUY Signal Detected")
elif signal == "SELL":
    st.error("🔻 SELL Signal Detected")
else:
    st.warning("⚠️ No Trade Setup")

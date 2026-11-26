import streamlit as st

st.set_page_config(page_title="SmartFlow AI", layout="wide")

st.title("SmartFlow AI")

st.metric("Market Structure", "Bullish")
st.metric("BOS", "Confirmed")
st.metric("CHOCH", "None")
st.metric("Signal", "BUY")

st.subheader("Risk Management")

account = 10000
risk = "1%"

st.write(f"Account Balance: ${account}")
st.write(f"Risk Per Trade: {risk}")

st.success("SmartFlow recommends BUY")

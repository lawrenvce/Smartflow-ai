import streamlit as st
from smc.market_data import get_market_data

st.set_page_config(
    page_title="SmartFlow AI",
    layout="wide"
)

st.title("SmartFlow AI")
st.write("AI-powered market analysis dashboard")

assets = {
    "XAUUSD": "GC=F",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "USDJPY": "JPY=X"
}

symbol = st.selectbox(
    "Choose Trading Pair",
    list(assets.keys())
)

if st.button("Load Market Data"):

    with st.spinner("Fetching market data..."):

        data = get_market_data(assets[symbol])

    if data is None or data.empty:
        st.error("No market data received. Please try again.")

    else:
        st.success(f"{symbol} market data loaded successfully!")

        st.subheader(f"{symbol} Market Data")

        st.dataframe(data.tail())

        st.subheader("Closing Price Chart")

        st.line_chart(data["Close"])


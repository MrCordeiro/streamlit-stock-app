import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Airbnb!
""")

tickerSymbol = "ABNB"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1d", start="2020-1-1", end="2021-1-17")

# tickerDf columns are: Open, Hign, Low, Close, Volume, Dividends, Stock, Splits

st.write("## Closing price")
st.line_chart(tickerDf.Close)
st.write("## Volume")
st.line_chart(tickerDf.Volume)

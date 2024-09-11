import streamlit as st
import yfinance as yf
import pandas as pd

# Set the title of the app
st.title("Stock Information Dashboard")

# Sidebar for stock selection
st.sidebar.header("Select Stock")
stock_symbol = st.sidebar.text_input("Enter stock ticker (e.g., AAPL, TSLA, MSFT)", value="AAPL")

# Get the stock data
@st.cache
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    return stock

# Fetch the data
stock_data = get_stock_data(stock_symbol)

# Display basic stock information
st.subheader(f"{stock_symbol.upper()} Stock Information")

# Get the stock info and display
info = stock_data.info
st.write("**Company Name:**", info.get('longName', 'N/A'))
st.write("**Sector:**", info.get('sector', 'N/A'))
st.write("**Industry:**", info.get('industry', 'N/A'))
st.write("**Market Cap:**", info.get('marketCap', 'N/A'))
st.write("**Previous Close:**", info.get('previousClose', 'N/A'))
st.write("**Open:**", info.get('open', 'N/A'))
st.write("**52 Week High:**", info.get('fiftyTwoWeekHigh', 'N/A'))
st.write("**52 Week Low:**", info.get('fiftyTwoWeekLow', 'N/A'))

# Fetch historical market data
st.subheader(f"Stock Price Data for {stock_symbol.upper()}")
period = st.sidebar.selectbox("Select period", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "5y", "10y", "ytd", "max"], index=6)
history = stock_data.history(period=period)

# Display the historical data in a table
st.write(history)

# Display historical data as a chart
st.line_chart(history['Close'])

# Display recent news
st.subheader(f"{stock_symbol.upper()} News")
news = stock_data.news
for article in news[:5]:  # Display top 5 news articles
    st.write(f"**{article['title']}**")
    st.write(article['link'])

# Sidebar info
st.sidebar.markdown("## About the app")
st.sidebar.info("This is a stock information dashboard built using Streamlit and yfinance.")

# Run the app using: streamlit run stock_app.py

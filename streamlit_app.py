import streamlit as st
import yfinance as yf
import pandas as pd

# Set the title of the app
st.title("Stock Information Dashboard")

# Sidebar for stock selection
st.sidebar.header("Select Stock")
stock_symbol = st.sidebar.text_input("Enter stock ticker (e.g., AAPL, TSLA, MSFT)", value="AAPL")

# Get the stock data
@st.cache_data
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    # Fetch only relevant data that is cacheable
    stock_info = stock.info
    history = stock.history(period='1y')  # For example, get 1 year of historical data
    return stock_info, history

# Fetch the data
try:
    stock_info, stock_history = get_stock_data(stock_symbol)

    # Display basic stock information
    st.subheader(f"{stock_symbol.upper()} Stock Information")
    st.write("**Company Name:**", stock_info.get('longName', 'N/A'))
    st.write("**Sector:**", stock_info.get('sector', 'N/A'))
    st.write("**Industry:**", stock_info.get('industry', 'N/A'))
    st.write("**Market Cap:**", stock_info.get('marketCap', 'N/A'))
    st.write("**Previous Close:**", stock_info.get('previousClose', 'N/A'))
    st.write("**52 Week High:**", stock_info.get('fiftyTwoWeekHigh', 'N/A'))
    st.write("**52 Week Low:**", stock_info.get('fiftyTwoWeekLow', 'N/A'))

    # Fetch historical market data
    st.subheader(f"Stock Price Data for {stock_symbol.upper()}")

    # Display the historical data in a table
    st.write(stock_history)

    # Display historical data as a chart
    st.line_chart(stock_history['Close'])

except Exception as e:
    st.error(f"An error occurred: {e}")

# Sidebar info
st.sidebar.markdown("## About the app")
st.sidebar.info("This is a stock information dashboard built using Streamlit and yfinance.")

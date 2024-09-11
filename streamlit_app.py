# streamlit_kospi_dashboard.py

import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# Title of the dashboard
st.title("KOSPI & KOSDAQ Stock Information Dashboard")

# Sidebar for input settings
st.sidebar.header("Settings")

# Select start and end date for historical data
start_date = st.sidebar.date_input("Start Date", datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())

# Function to get stock data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(start=start_date, end=end_date)

# Fetching KOSPI and KOSDAQ data
kospi_data = get_stock_data("^KS11")  # KOSPI Index ticker
kosdaq_data = get_stock_data("^KQ11")  # KOSDAQ Index ticker

# Display KOSPI and KOSDAQ indices with chart
st.subheader("KOSPI Index")
st.line_chart(kospi_data['Close'])

st.subheader("KOSDAQ Index")
st.line_chart(kosdaq_data['Close'])

# Calculate the percentage change for KOSPI and KOSDAQ
kospi_change = ((kospi_data['Close'][-1] - kospi_data['Close'][0]) / kospi_data['Close'][0]) * 100
kosdaq_change = ((kosdaq_data['Close'][-1] - kosdaq_data['Close'][0]) / kosdaq_data['Close'][0]) * 100

# Display percentage increase rates
st.write(f"**KOSPI Increase Rate**: {kospi_change:.2f}%")
st.write(f"**KOSDAQ Increase Rate**: {kosdaq_change:.2f}%")

# Function to get top gainers and losers from the KOSPI market
def get_top_movers(index_ticker, top_n=5):
    # Get the components of the index (here we'll simulate a few stocks for demonstration)
    tickers = ['005930.KS', '000660.KS', '035420.KS', '005380.KS', '051910.KS']  # Samsung, SK Hynix, NAVER, Hyundai, LG
    stock_data = {ticker: yf.Ticker(ticker).history(period="1d")['Close'].iloc[-1] for ticker in tickers}

    # Convert the dictionary into a DataFrame
    stock_df = pd.DataFrame(list(stock_data.items()), columns=['Ticker', 'Close'])
    stock_df['Change (%)'] = stock_df['Close'].pct_change() * 100

    # Get top gainers and losers
    top_gainers = stock_df.sort_values(by='Change (%)', ascending=False).head(top_n)
    top_losers = stock_df.sort_values(by='Change (%)').head(top_n)

    return top_gainers, top_losers

# Fetch top movers in the KOSPI market
st.subheader("Top Gainers and Losers in KOSPI")
top_gainers, top_losers = get_top_movers("^KS11")

# Display top gainers
st.write("### Top Gainers")
st.dataframe(top_gainers)

# Display top losers
st.write("### Top Losers")
st.dataframe(top_losers)

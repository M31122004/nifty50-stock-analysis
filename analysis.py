import streamlit as st
import pandas as pd

# Dashboard Title
st.title("📊 NIFTY50 Stock Analysis Dashboard")

# Load Dataset
df = pd.read_csv("stocks.csv")

# Convert date column into datetime format
df["date"] = pd.to_datetime(df["date"])

# Sort data by symbol and date
df = df.sort_values(["symbol", "date"])

# Calculate daily return
df["daily_return"] = df.groupby("symbol")["close"].pct_change()

# Calculate volatility
volatility = df.groupby("symbol")["daily_return"].std()

# Top 10 volatile stocks
top_volatility = volatility.sort_values(ascending=False).head(10)

# Display Top Volatile Stocks
st.subheader("🔥 Top 10 Volatile Stocks")
st.write(top_volatility)

# Calculate yearly return
first_price = df.groupby("symbol")["close"].first()
last_price = df.groupby("symbol")["close"].last()

yearly_return = (last_price - first_price) / first_price

# Top 10 Green Stocks
top_green = yearly_return.sort_values(ascending=False).head(10)

st.subheader("📈 Top 10 Green Stocks")
st.write(top_green)

# Top 10 Red Stocks
top_red = yearly_return.sort_values().head(10)

st.subheader("📉 Top 10 Red Stocks")
st.write(top_red)
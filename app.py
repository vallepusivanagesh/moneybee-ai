import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title="MoneyBee",
    page_icon="🐝",
    layout="wide"
)

st.title("🐝 MoneyBee")
st.subheader("AI Financial Intelligence")
st.write("Smarter Insights. Better Investments.")

st.divider()

st.header("📊 Company Stock Research")

symbol = st.text_input(
    "Enter NSE stock ticker",
    placeholder="Example: RELIANCE.NS"
)

@st.cache_data(ttl=300)
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    history = stock.history(period="1y")

    if history.empty:
        return None

    return history

if st.button("Analyse Company"):
    if not symbol.strip():
        st.warning("Please enter a stock ticker.")
    else:
        ticker = symbol.strip().upper()

        with st.spinner("Fetching stock market data..."):
            try:
                history = get_stock_data(ticker)

                if history is None:
                    st.error("Stock data not found. Check the ticker.")
                else:
                    latest = history["Close"].iloc[-1]
                    previous = history["Close"].iloc[-2]
                    change = latest - previous
                    change_percent = (change / previous) * 100

                    st.success(f"Research report: {ticker}")

                    col1, col2, col3 = st.columns(3)

                    col1.metric(
                        "Latest Price",
                        f"₹{latest:,.2f}",
                        f"{change_percent:.2f}%"
                    )

                    col2.metric(
                        "52-Week High",
                        f"₹{history['High'].max():,.2f}"
                    )

                    col3.metric(
                        "52-Week Low",
                        f"₹{history['Low'].min():,.2f}"
                    )

                    st.subheader("📈 1-Year Stock Price Chart")
                    st.line_chart(history["Close"])

                    st.subheader("Latest Market Data")
                    st.dataframe(
                        history.tail(10),
                        use_container_width=True
                    )

                    st.caption(
                        "Source: Yahoo Finance via yfinance. "
                        "Data may be delayed or incomplete."
                    )

            except Exception as e:
                st.error(f"Unable to fetch data: {e}")

st.divider()

st.header("🐝 MoneyBee Intelligence Modules")

col1, col2 = st.columns(2)

with col1:
    st.write("📊 Company Financial Analysis")
    st.write("📈 Stock Market Research")
    st.write("🏦 FII & DII Tracking")
    st.write("💰 Investor Holdings")

with col2:
    st.write("🚀 IPO Intelligence")
    st.write("🎯 Analyst Target Prices")
    st.write("⚠️ Risk Analysis")
    st.write("🌐 Telugu & English Reports")

st.divider()

st.caption(
    "MoneyBee | Financial research, not investment advice."
)


import streamlit as st

st.set_page_config(
    page_title="MoneyBee",
    page_icon="🐝",
    layout="wide"
)

st.title("🐝 MoneyBee")
st.subheader("AI Financial Intelligence")

st.write("Smarter Insights. Better Investments.")

st.divider()

company = st.text_input(
    "Search a company",
    placeholder="Example: Reliance Industries"
)

if st.button("Analyse Company"):
    if company:
        st.success(f"Research workspace: {company}")
        st.info("AI financial research module will be connected next.")
    else:
        st.warning("Please enter a company name.")

st.divider()

st.header("Our Intelligence Modules")

col1, col2 = st.columns(2)

with col1:
    st.write("📊 Company Financial Analysis")
    st.write("📈 Stock Research")
    st.write("🏦 FII & DII Tracking")
    st.write("💰 Investor Holdings")

with col2:
    st.write("🚀 IPO Intelligence")
    st.write("🎯 Analyst Target Prices")
    st.write("⚠️ Risk Analysis")
    st.write("🌐 Telugu & English Reports")

st.divider()
st.caption("MoneyBee | Financial Intelligence Platform")
st.caption("Research information is not investment advice.")

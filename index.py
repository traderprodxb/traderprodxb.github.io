import streamlit as st

# Page Configuration
st.set_page_config(page_title="Akbar's Blueprint", layout="wide")

# Simple Header
st.title("Trading Blueprint")
st.write("Welcome to your machine-like trading dashboard.")

# Metrics Section
col1, col2, col3 = st.columns(3)
col1.metric("Daily Target", "12% ROI")
col2.metric("Stop Loss", "6% ROI")
col3.metric("Goal", "4,000,000 USDT")

# Content Section
st.subheader("Strategy Logic")
st.text("1. Machine-like execution.\n2. Five trades per day.\n3. Reinvest for compounding.")

if st.button("Calculate Next Trade"):
    st.success("System ready for next position sizing.")

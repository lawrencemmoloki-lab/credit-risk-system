import streamlit as st
from src.connect_db import engine
import pandas as pd

st.title("Credit Risk Intelligence System")

@st.cache_data
def load_data():
    return pd.read_sql("SELECT * FROM loans", engine)

df = load_data()

st.markdown("##  Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Loans", len(df))
col2.metric("Default Rate (%)", round(df["default_status"].mean() * 100, 2))
col3.metric("Avg Credit", round(df["credit_amount"].mean(), 2))

st.markdown("### Risk Distribution")
st.bar_chart(df["default_status"].value_counts())
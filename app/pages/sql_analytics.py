import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import urllib.parse

# --- SMART DATABASE CONNECTION ---
load_dotenv()

# This reads from local .env file OR Streamlit Cloud Secrets
DB_HOST = os.getenv("DB_HOST") or st.secrets.get("DB_HOST")
DB_NAME = os.getenv("DB_NAME") or st.secrets.get("DB_NAME")
DB_USER = os.getenv("DB_USER") or st.secrets.get("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD") or st.secrets.get("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT") or st.secrets.get("DB_PORT")

# Safely encode the password (fixes the @ symbol issue)
encoded_password = urllib.parse.quote_plus(DB_PASSWORD) if DB_PASSWORD else ""

DATABASE_URL = f"postgresql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
# -------------------------------------------

st.title("SQL Analytics Dashboard")

st.markdown("Real-time business insights pulled directly from the PostgreSQL database.")

# Query 1: Default risk by housing
st.subheader("1. Default Risk by Housing Type")
try:
    query1 = """
    SELECT housing, AVG(default_status) AS default_rate
    FROM customers c
    JOIN loans l ON c.customer_id = l.customer_id
    GROUP BY housing
    ORDER BY default_rate DESC;
    """
    df1 = pd.read_sql(query1, engine)
    st.dataframe(df1)
    st.bar_chart(df1, x="housing", y="default_rate")
except Exception as e:
    st.error(f"Error: {e}")

# Query 2: Average loan amount by employment
st.subheader("2. Average Loan Amount by Employment Status")
try:
    query2 = """
    SELECT employment, AVG(credit_amount) AS avg_credit_amount
    FROM loans
    GROUP BY employment
    ORDER BY avg_credit_amount DESC;
    """
    df2 = pd.read_sql(query2, engine)
    st.dataframe(df2)
    st.bar_chart(df2, x="employment", y="avg_credit_amount")
except Exception as e:
    st.error(f"Error: {e}")

# Query 3: Highest-risk purposes
st.subheader("3. Highest-Risk Loan Purposes")
try:
    query3 = """
    SELECT purpose, AVG(default_status) AS risk_rate
    FROM loans
    GROUP BY purpose
    ORDER BY risk_rate DESC;
    """
    df3 = pd.read_sql(query3, engine)
    st.dataframe(df3)
    st.bar_chart(df3, x="purpose", y="risk_rate")
except Exception as e:
    st.error(f"Error: {e}")
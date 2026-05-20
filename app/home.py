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

st.title("Credit Risk Intelligence System")

# Fetch data
with st.spinner("Loading data from Supabase..."):
    try:
        query = """
        SELECT c.age, c.housing, c.job, 
               l.checking_status, l.duration, l.credit_history, l.purpose, 
               l.credit_amount, l.savings_status, l.employment, l.default_status
        FROM customers c 
        JOIN loans l ON c.customer_id = l.customer_id
        """
        df = pd.read_sql(query, engine)
        st.success("Data loaded successfully!")
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        df = pd.DataFrame() # Empty dataframe if connection fails

if not df.empty:
    # Show raw data
    st.subheader("Raw Data Preview")
    st.dataframe(df.head(20))

    # Show default rate by housing
    st.subheader("Default Rate by Housing Type")
    housing_risk = df.groupby("housing")["default_status"].mean().reset_index()
    st.bar_chart(housing_risk, x="housing", y="default_status")

    # Show average loan amount
    st.subheader("Average Credit Amount by Purpose")
    purpose_amount = df.groupby("purpose")["credit_amount"].mean().reset_index()
    st.bar_chart(purpose_amount, x="purpose", y="credit_amount")
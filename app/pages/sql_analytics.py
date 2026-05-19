import streamlit as st
import pandas as pd
from src.connect_db import engine

st.title("SQL Analytics Dashboard")

def run_query(q):
    return pd.read_sql(q, engine)

# 1. Default rate by employment
st.markdown("Default Rate by Employment")

q1 = """
SELECT employment, AVG(default_status) AS default_rate
FROM loans
GROUP BY employment
ORDER BY default_rate DESC;
"""

df1 = run_query(q1)
st.bar_chart(df1.set_index("employment"))

# 2. Credit history risk
st.markdown("Risk by Credit History")

q2 = """
SELECT credit_history, AVG(default_status) AS default_rate
FROM loans
GROUP BY credit_history;
"""

df2 = run_query(q2)
st.bar_chart(df2.set_index("credit_history"))

# 3. Loan size vs risk
st.markdown("Loan Size vs Default")

q3 = """
SELECT default_status, AVG(credit_amount) AS avg_loan
FROM loans
GROUP BY default_status;
"""

df3 = run_query(q3)
st.bar_chart(df3.set_index("default_status"))
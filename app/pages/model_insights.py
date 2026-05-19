import streamlit as st
import pickle
import pandas as pd

st.title(" Model Insights")

model = pickle.load(open("src/model.pkl", "rb"))

# Feature importance
st.markdown("### Feature Importance")

features = [
    "duration",
    "credit_amount",
    "age",
    "installment_rate",
    "existing_credits"
]

importance = model.feature_importances_

df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

st.bar_chart(df.set_index("Feature"))

# Basic model info
st.markdown("### ℹ Model Type")
st.write(type(model).__name__)
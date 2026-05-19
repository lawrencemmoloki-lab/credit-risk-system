import streamlit as st
import pickle
import pandas as pd
from pathlib import Path

st.title("Model Insights")

# FIX 1: Use pathlib to find the correct path on Streamlit Cloud
ROOT_DIR = Path(__file__).parent.parent.parent
MODEL_PATH = ROOT_DIR / "src" / "model.pkl"

try:
    model = pickle.load(open(MODEL_PATH, "rb"))
except FileNotFoundError:
    st.error(f"Model file not found! Looked at: {MODEL_PATH}. Make sure you pushed it to GitHub!")
    st.stop()

# Feature importance
st.markdown("Feature Importance")

# FIX 2: Ensure these match EXACTLY the 4 features we trained the model on!
features = [
    "duration",
    "credit_amount",
    "age",
    "installment_rate"
]

importance = model.feature_importances_

df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

st.bar_chart(df.set_index("Feature"))

# Basic model info
st.markdown("Model Type")
st.write(type(model).__name__)
import streamlit as st
import pickle
import pandas as pd
from pathlib import Path

st.title("Model Insights")

# Path fix
ROOT_DIR = Path(__file__).parent.parent.parent
MODEL_PATH = ROOT_DIR / "src" / "model.pkl"

try:
    model = pickle.load(open(MODEL_PATH, "rb"))
except FileNotFoundError:
    st.error(f"Model file not found! Looked at: {MODEL_PATH}. Make sure you pushed it to GitHub!")
    st.stop()

# Feature importance
st.markdown("Feature Importance")

# FIX: Automatically get the feature names directly from the trained model!
# This guarantees the lists are the exact same length.
try:
    features = list(model.feature_names_in_)
except AttributeError:
    # Fallback just in case
    features = ["duration", "credit_amount", "age", "installment_rate"]

importance = model.feature_importances_

df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

st.bar_chart(df.set_index("Feature"))

# Basic model info
st.markdown("Model Type")
st.write(type(model).__name__)
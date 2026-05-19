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

importance = model.feature_importances_

# SAFE FIX: Dynamically get the exact number of features the model expects
if hasattr(model, 'feature_names_in_'):
    features = list(model.feature_names_in_)
else:
    # If the model doesn't have names stored, create generic names to match the length
    features = [f"Feature_{i+1}" for i in range(len(importance))]

df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

st.bar_chart(df.set_index("Feature"))

# Basic model info
st.markdown(" Model Type")
st.write(type(model).__name__)
import streamlit as st
import pickle
import numpy as np
from pathlib import Path

st.title("Credit Risk Prediction")

# FIX 1: Use pathlib to find the correct path on Streamlit Cloud
ROOT_DIR = Path(__file__).parent.parent.parent
MODEL_PATH = ROOT_DIR / "src" / "model.pkl"

try:
    model = pickle.load(open(MODEL_PATH, "rb"))
except FileNotFoundError:
    st.error(f"Model file not found! Looked at: {MODEL_PATH}. Make sure you pushed it to GitHub!")
    st.stop()

# FIX 2: Only use the 4 features the model was trained on!
duration = st.slider("Loan Duration (months)", 1, 72, 12)
credit = st.number_input("Credit Amount ($)", 100, 100000, 5000, step=500)
age = st.slider("Age", 18, 100, 30)
installment = st.slider("Installment Rate", 1, 4, 2)

if st.button("Predict Risk", type="primary"):
    # Make sure the array only has 4 columns to match the model
    X = np.array([[duration, credit, age, installment]])

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]

    if prob < 0.3:
        st.success("🟢 LOW RISK")
    elif prob < 0.7:
        st.warning("🟠 MEDIUM RISK")
    else:
        st.error("🔴 HIGH RISK")

    st.write(f"**Default Probability:** {prob * 100:.1f}%")
    st.progress(int(prob * 100))
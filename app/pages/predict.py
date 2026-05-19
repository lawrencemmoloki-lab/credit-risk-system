import streamlit as st
import pickle
import numpy as np

st.title("Credit Risk Prediction")

model = pickle.load(open("src/model.pkl", "rb"))

duration = st.slider("Duration", 1, 72, 12)
credit = st.number_input("Credit Amount", 100, 100000, 5000)
age = st.slider("Age", 18, 100, 30)
installment = st.slider("Installment Rate", 1, 4, 2)
existing = st.slider("Existing Credits", 1, 4, 1)

if st.button("Predict"):

    X = np.array([[duration, credit, age, installment, existing]])

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]

    if prob < 0.3:
        st.success("🟢 LOW RISK")
    elif prob < 0.7:
        st.warning("🟠 MEDIUM RISK")
    else:
        st.error("🔴 HIGH RISK")

    st.write("Probability:", round(prob, 2))
    st.progress(int(prob * 100))
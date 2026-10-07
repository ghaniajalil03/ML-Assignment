import streamlit as st
import pickle

st.set_page_config(page_title="Salary Predictor", page_icon="💸")
st.header("ML-Assignment")

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

YoE= st.number_input('Years of Experience', min_value=0.0, max_value=1.0, step=0.5, value=2.0)


if st.button("Predict Salary"):
    prediction= model.predict([[YoE]])
  st.success(prediction)

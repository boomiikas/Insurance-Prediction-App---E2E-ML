import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('trained_model.sav', 'rb'))

st.title("Insurance Charges Prediction App")

st.write("Enter the details below to predict insurance charges:")

age = st.number_input("Age:", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI:", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of children:", min_value=0, max_value=10, value=0)
gender = st.selectbox("Gender:", ["Female", "Male"])
smoker = st.selectbox("Smoker:", ["No", "Yes"])

gender_male = 1 if gender == "Male" else 0
smoker_yes = 1 if smoker == "Yes" else 0

features = np.array([[age, bmi, children, gender_male, smoker_yes]])

if st.button("Predict Charges"):
    prediction = float(model.predict(features)[0])  # convert to float
    st.success(f"Estimated Insurance Charges: ${prediction:,.2f}")


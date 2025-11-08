import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.set_page_config(page_title="Sleep Disorder Prediction", page_icon="💤", layout="centered")

# model = joblib.load('')
joblib.load("best_sleep_model.joblib")

st.title("💤 Sleep Health & Lifestyle Prediction App")
st.write("Provide your lifestyle and health details to predict your sleep health status.")

# --- User Inputs ---
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 80, 25)
occupation = st.selectbox(
    "Occupation",
    ["Software Engineer", "Doctor", "Teacher", "Nurse", "Sales Representative",
     "Accountant", "Lawyer", "Engineer", "Manager", "Student", "Other"]
)
sleep_duration = st.number_input("Sleep Duration (hours)", 0.0, 12.0, 7.0, 0.5)
quality_of_sleep = st.slider("Quality of Sleep (1 = Poor, 10 = Excellent)", 1, 10, 7)
physical_activity = st.slider("Physical Activity Level (minutes/day)", 0, 300, 30)
stress_level = st.slider("Stress Level (1 = Low, 10 = High)", 1, 10, 5)
bmi_category = st.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obese"])
blood_pressure = st.text_input("Blood Pressure (e.g. 120/80)")
heart_rate = st.number_input("Heart Rate (BPM)", 40, 180, 75)
daily_steps = st.number_input("Daily Steps", 0, 30000, 5000)

# --- Convert Blood Pressure ---
def parse_bp(bp):
    try:
        sys, dia = bp.split('/')
        return int(sys), int(dia)
    except:
        return 120, 80  # default if invalid input

sys_bp, dia_bp = parse_bp(blood_pressure)

# --- Prepare Input Data ---
input_data = pd.DataFrame({
    "Gender": [gender],
    "Age": [age],
    "Occupation": [occupation],
    "Sleep Duration": [sleep_duration],
    "Quality of Sleep": [quality_of_sleep],
    "Physical Activity Level": [physical_activity],
    "Stress Level": [stress_level],
    "BMI Category": [bmi_category],
    "Systolic_BP": [sys_bp],
    "Diastolic_BP": [dia_bp],
    "Heart Rate": [heart_rate],
    "Daily Steps": [daily_steps]
})

st.subheader("📋 Input Summary")
st.dataframe(input_data)

# --- Prediction Section ---
st.subheader("🧠 Sleep Disorder Prediction")

# Load model (optional)
# model = joblib.load("sleep_model.pkl")

if st.button("Predict Sleep Disorder"):
    # Replace this dummy prediction logic with your ML model prediction
    # prediction = model.predict(input_data)[0]

    # Dummy logic example (replace with your model)
    if sleep_duration < 5 or stress_level > 7:
        prediction = "Likely Insomnia"
    elif quality_of_sleep < 5:
        prediction = "Possible Sleep Apnea"
    else:
        prediction = "Normal Sleep"

    st.success(f"### 🩺 Prediction: **{prediction}**")

# st.write("---")
# st.caption("Developed with ❤️ using Streamlit and Machine Learning.")

import streamlit as st
import time

st.set_page_config(page_title="BMI CALCULATOR MADE BY RIZWANA", page_icon="m", layout="centered")

st.title("⚖️ BMI CALCULATOR IN PYTHON WITH STREAMLIT")
st.markdown("""**Enter your body weight and height** """)

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, step=1.0, format="%.2f")
with col2:
    height = st.number_input("Height (m):", min_value=1.0, step=0.01, format="%.2f")

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.subheader("Your BMI is:")
        st.markdown(f"{bmi:.2f}", unsafe_allow_html=True)

        if bmi < 18.5:
            st.error("Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Overweight")
        else:
            st.error("Obesity")
    else:
        st.info("Please enter a valid number")

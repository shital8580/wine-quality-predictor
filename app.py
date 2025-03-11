import streamlit as st
import joblib
import numpy as np

# Load trained model & scaler
model = joblib.load("xgb_wine_quality.pkl")
scaler = joblib.load("scaler.pkl")  # Load the same scaler used during training

# Streamlit UI
st.title("🍷 Wine Quality Prediction App")

st.write("Enter the wine characteristics below to predict its quality:")

# User input fields
fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, max_value=20.0, value=7.0)
volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, max_value=2.0, value=0.3)
citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=2.0, value=0.4)
residual_sugar = st.number_input("Residual Sugar", min_value=0.0, max_value=50.0, value=2.0)
chlorides = st.number_input("Chlorides", min_value=0.0, max_value=1.0, value=0.05)
free_sulfur = st.number_input("Free Sulfur Dioxide", min_value=0, max_value=300, value=30)
total_sulfur = st.number_input("Total Sulfur Dioxide", min_value=0, max_value=500, value=120)
density = st.number_input("Density", min_value=0.98, max_value=1.02, value=0.995)
pH = st.number_input("pH", min_value=2.5, max_value=4.5, value=3.2)
sulphates = st.number_input("Sulphates", min_value=0.0, max_value=2.0, value=0.5)
alcohol = st.number_input("Alcohol", min_value=5.0, max_value=20.0, value=10.0)
wine_type = st.selectbox("Wine Type", ["White", "Red"])  # Dropdown for wine type

# Convert wine type to numerical value
wine_type_num = 0 if wine_type == "White" else 1

# Predict button
if st.button("Predict Quality"):
    # Convert input to array (Match Feature Order Used in Training)
    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
                            chlorides, free_sulfur, total_sulfur, density, pH, sulphates, 
                            alcohol, wine_type_num]])

    # Apply Standard Scaling
    input_scaled = scaler.transform(input_data)

    # Make prediction and shift back
    predicted_quality = model.predict(input_scaled)[0] + 3  # Shift back to original scale

    # Show result
    st.success(f"🍾 Predicted Wine Quality: **{int(predicted_quality)}**")

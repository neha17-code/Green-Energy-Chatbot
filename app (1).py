import streamlit as st
import pandas as pd
import joblib

# Load model and training columns
saved_data = joblib.load("model.pkl")
model = saved_data["model"]
columns = saved_data["columns"]

st.title("🌱 Sustainability Score Prediction System")

# Product Type
product_type = st.selectbox(
    "Select Product Type",
    ["Automotive", "Pharmaceutical", "Food", "Apparel", "Electronics"]
)

# Numeric Inputs
raw_material = st.number_input("Raw Material Usage (kg)", min_value=0.0)
energy_consumption = st.number_input("Energy Consumption (kWh)", min_value=0.0)
waste_generated = st.number_input("Waste Generated (kg)", min_value=0.0)
transport_distance = st.number_input("Transport Distance (km)", min_value=0.0)
co2_emissions = st.number_input("CO2 Emissions (kg)", min_value=0.0)
manufacturing_energy = st.number_input("Manufacturing Energy (kWh)", min_value=0.0)
renewable_energy = st.number_input("Renewable Energy (%)", min_value=0.0)
cost = st.number_input("Cost ($)", min_value=0.0)
delivery_time = st.number_input("Delivery Time (days)", min_value=0.0)

# PREDICTION BUTTON
if st.button("Predict Sustainability Score"):

    # Create input dictionary
    input_data = {col: 0 for col in columns}

    # Encode product type
    product_column = f"Product_Type_{product_type}"
    if product_column in input_data:
        input_data[product_column] = 1

    # Assign numeric values
    input_data["Raw_Material_Usage_kg"] = raw_material
    input_data["Energy_Consumption_kWh"] = energy_consumption
    input_data["Waste_Generated_kg"] = waste_generated
    input_data["Transport_Distance_km"] = transport_distance
    input_data["CO2_Emissions_kg"] = co2_emissions
    input_data["Manufacturing_Energy_kWh"] = manufacturing_energy
    input_data["Renewable_Energy_%"] = renewable_energy
    input_data["Cost_$"] = cost
    input_data["Delivery_Time_days"] = delivery_time

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict
    prediction = model.predict(input_df)

    st.success(f"Predicted Sustainability Score: {prediction[0]:.2f}")

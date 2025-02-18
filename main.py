import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('water_quality_prediction_system.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the prediction function
def predict_quality(pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity):
    features = np.array([[pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    prediction = model.predict(features)
    return 'Safe' if prediction[0] == 1 else 'Unsafe'

# Streamlit UI

# let's create a function to define the web page
def main():
    # front end elements of the web page
    html_temp = """ 
        <div style ="background-color:blue;padding:15px"> 
        <h1 style ="color:black;text-align:center;">Groundwater Quality Prediction</h1> 
        </div> 
        """

st.title("Groundwater Quality Prediction")
st.image("groundwater.jpg", caption="Groundwater Quality Monitoring", use_column_width=True)


# Enter all the parameters of water
st.header("Enter the characteristics of the water:")
col1, col2, col3 = st.columns(3)

with col1:
    pH = st.number_input("pH Level", min_value=5.0, max_value=9.0, value=7.0, step=0.1)
    Hardness = st.number_input("Hardness (mg/L)", min_value=0.0, max_value=500.0, value=100.0, step=1.0)
    Solids = st.number_input("Solids (ppm)", min_value=0.0, max_value=50000.0, value=15000.0, step=100.0)

with col2:
    Chloramines = st.number_input("Chloramines (mg/L)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
    Sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, max_value=500.0, value=250.0, step=1.0)
    Conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, max_value=2000.0, value=500.0, step=10.0)

with col3:
    Organic_carbon = st.number_input("Organic Carbon (mg/L)", min_value=0.0, max_value=30.0, value=10.0, step=0.5)
    Trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    Turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, max_value=10.0, value=2.5, step=0.1)

if st.button("Predict Quality"):
    result = predict_quality(pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity)
    st.success(f"The predicted water quality is: {result}")

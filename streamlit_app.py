import pandas as pd
import streamlit as st
import pickle
from PIL import Image

with open("xgboost_model.sav","rb") as file:
    model = pickle.load(file)

image = Image.open("pm25_banner.jpeg")
st.image(image,use_container_width=True)
#st.title("PM2.5 Prediction")

st.subheader("Enter Atmospheric and Meteorological Values")

col1, col2, col3 = st.columns(3)

with col1:
    co = st.number_input("Carbon Monoxide (CO)")
    aermr04 = st.number_input("Dust Aerosol (0.03–0.55 µm)")
    aermr05 = st.number_input("Dust Aerosol (0.55–0.9 µm)")
    aermr06 = st.number_input("Dust Aerosol (0.9–20 µm)")
    aermr09 = st.number_input("Hydrophilic Black Carbon")
    aermr07 = st.number_input("Hydrophilic Organic Matter")

with col2:
    aermr10 = st.number_input("Hydrophobic Black Carbon")
    aermr08 = st.number_input("Hydrophobic Organic Matter")
    no2 = st.number_input("Nitrogen Dioxide (NO₂)")
    no = st.number_input("Nitrogen Monoxide (NO)")
    go3 = st.number_input("Ozone (O₃)")
    so2 = st.number_input("Sulphur Dioxide (SO₂)")

with col3:
    q = st.number_input("Specific Humidity")
    t = st.number_input("Temperature")
    u10 = st.number_input("10 m U-Wind Component")
    v10 = st.number_input("10 m V-Wind Component")
    d2m = st.number_input("2 m Dew Point Temperature")
    t2m = st.number_input("2 m Temperature")

comp_met_variables = [
    'co',
    'aermr04',
    'aermr05',
    'aermr06',
    'aermr09',
    'aermr07',
    'aermr10',
    'aermr08',
    'no2',
    'no',
    'go3',
    'so2',
    'q',
    't',
    'u10',
    'v10',
    'd2m',
    't2m'
]


input_data = pd.DataFrame([[
    co,
    aermr04,
    aermr05,
    aermr06,
    aermr09,
    aermr07,
    aermr10,
    aermr08,
    no2,
    no,
    go3,
    so2,
    q,
    t,
    u10,
    v10,
    d2m,
    t2m
]], 
columns=comp_met_variables)

if st.button("Predict PM2.5"):
    prediction = model.predict(input_data)
    st.success(f"Predicted PM2.5: {prediction[0]:.2f} µg/m³")


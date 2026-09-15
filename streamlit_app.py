import pandas as pd
import streamlit as st
import pickle

with open("xgboost_model.sav","rb") as file:
    model = pickle.load(file)

st.title("PM2.5 Prediction")

st.subheader("Enter Atmospheric and Meteorological Values")

co = st.number_input("CO")
aermr04 = st.number_input("Aerosol AERMR04")
aermr05 = st.number_input("Aerosol AERMR05")
aermr06 = st.number_input("Aerosol AERMR06")
aermr09 = st.number_input("Aerosol AERMR09")
aermr07 = st.number_input("Aerosol AERMR07")
aermr10 = st.number_input("Aerosol AERMR10")
aermr08 = st.number_input("Aerosol AERMR08")
no2 = st.number_input("NO2")
no = st.number_input("NO")
go3 = st.number_input("Ozone (GO3)")
so2 = st.number_input("SO2")
q = st.number_input("Specific Humidity (Q)")
t = st.number_input("Temperature (T)")
u10 = st.number_input("U10")
v10 = st.number_input("V10")
d2m = st.number_input("2m Dew Point (D2M)")
t2m = st.number_input("2m Temperature (T2M)")

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


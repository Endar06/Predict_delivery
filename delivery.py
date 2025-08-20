import warnings
warnings.filterwarnings('ignore')

import streamlit as st
import joblib
import numpy as np
import os
import gdown
from streamlit_option_menu import option_menu

def delivery_predict():

   
    model = joblib.load("model_predict.pkl")

    st.title('ESTIMASI WAKTU DELIVERY')
    st.image("https://blog.ipleaders.in/wp-content/uploads/2019/11/foodmitho.jpg", width=150)

    col1, col2 = st.columns(2)

    with col1:
        Distance_km = st.number_input("Jarak (per Km²)", min_value=0)
        Preparation_Time_min = st.number_input("Waktu Persiapan", min_value=0)
        Courier_Experience_yrs = st.number_input('Tahun pengalaman kurir', min_value=0)

    with col2:
        Weather_input = st.selectbox(
            "Pilih Kondisi Cuaca:",
            ["Cuaca Cerah", "Cuaca Hujan", "Cuaca Berkabut", "Cuaca Bersalju","Cuaca Berangin"]
        )
        Cuaca_mapping = {
            "Cuaca Cerah": 0,
            "Cuaca Hujan": 2,
            "Cuaca Berkabut": 1,
            "Cuaca Bersalju": 4,
            "Cuaca Berangin": 3
        }
        Weather = Cuaca_mapping[Weather_input]
        hari_input = st.selectbox(
            "Pilih Kondisi Hari:",
            ["Pagi Hari", "Siang Hari", "Sore Hari", "Malam Hari"]
        )
        kondisi_hari = {
            "Pagi Hari": 2,
            "Siang Hari": 1,
            "Sore Hari": 0,
            "Malam Hari": 3
        }
        Time_of_Day = kondisi_hari[hari_input]
        kendaraan_input = st.selectbox(
            "Pilih jenis kendaraan:",
            ["Bike", "Scooter", "Car"]
        )
        jenis_kendaraan = {
            "Bike": 0,
            "Scooter": 2,
            "Car": 1
        }
        Vehicle_Type = jenis_kendaraan[kendaraan_input]
        traffic_input = st.selectbox(
            "Pilih Kondisi Lalulintas:",
            ["Low", "Medium", "High"]
        )
        kondisi_traffic = {
            "Low": 1,
            "Medium": 2,
            "High": 0
        }
        Traffic_Level = kondisi_traffic[traffic_input]
 

    if st.button('🔍 Estimasi Waktu Delivery'):
        input_data = np.array([[Distance_km, Weather, Traffic_Level, Time_of_Day, Vehicle_Type, Preparation_Time_min,
                                Courier_Experience_yrs]])
        
        predict = model.predict(input_data)[0]

        st.success(f"⏱ Estimasi Waktu Delivery: {round(predict)} menit")

        
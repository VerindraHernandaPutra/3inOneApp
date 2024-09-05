import streamlit as st
import pages.weather.Function as function
import pickle
import numpy as np
import pandas as pd

# Ambil Dataset hasil modifikasi
dataset = pd.read_csv("Dataset_Final/weather_modified.csv")
X = dataset.drop(columns = ['Weather Type'], axis=1)

Weather = ['Sunny', 'Cloudy', 'Rainy', 'Snowy']
Image = ['Asset/Sunny.jpg', 'Asset/Cloudy.jpg', 'Asset/Rainy.jpg', 'Asset/Snowy.jpg']

with open("weather.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def main():
    st.sidebar.title('Input')

    # Temperature
    Temperature = st.sidebar.text_input("Temperature", placeholder="Silahkan masukkan angka..")
    Temperature = function.handle_empty_input(Temperature)

    # Kelembaban
    Humidity = st.sidebar.text_input("Kelembaban", placeholder="Silahkan masukkan angka..")
    Humidity = function.handle_empty_input(Humidity)

    # Kecepatan Angin
    Wind_Speed = st.sidebar.text_input("Kecepatan Angin", placeholder="Silahkan masukkan angka..")
    Wind_Speed = function.handle_empty_input(Wind_Speed)

    # Pengendapan (%)
    Precipitation = st.sidebar.text_input("Pengendapan (%)", placeholder="Silahkan masukkan angka..")
    Precipitation = function.handle_empty_input(Precipitation)

    # Kondisi langit
    Cloud_Cover = st.sidebar.selectbox(
        "Kondisi langit",
        ('clear', 'partly cloudy', 'cloudy', 'overcast'),
        index=None,
        placeholder="Silahkan pilih..",
    )
    Cloud_Cover = function.pilih_Cloud_Cover(Cloud_Cover)

    # Tekanan Atmosfer
    Atmospheric_Pressure = st.sidebar.text_input("Tekanan Atmosfer", placeholder="Silahkan masukkan angka..")
    Atmospheric_Pressure = function.handle_empty_input(Atmospheric_Pressure)

    # Indeks UV
    UV_index = st.sidebar.text_input("Indeks UV", placeholder="Silahkan masukkan angka..")
    UV_index = function.handle_empty_input(UV_index)

    # Musim
    Season = st.sidebar.selectbox(
        "Musim",
        ('Spring', 'Summer', 'Autumn', 'Winter'),
        index=None,
        placeholder="Silahkan pilih..",
    )
    Season = function.pilih_Season(Season)

    # Jarak pandang (km)
    Visibility = st.sidebar.text_input("Jarak pandang (km)", placeholder="Silahkan masukkan angka..")
    Visibility = function.handle_empty_input(Visibility)

    # Lokasi
    Location = st.sidebar.selectbox(
        "Location",
        ('Coastal', 'Inland', 'Mountain'),
        index=None,
        placeholder="Silahkan pilih..",
    )
    Location = function.pilih_Location(Location)

    # Prediksi
    input = np.array([Temperature, Humidity, Wind_Speed, Precipitation, Cloud_Cover, Atmospheric_Pressure, UV_index, Season, Visibility, Location])
    input = np.expand_dims(input, axis = 0)
    predict = model.predict_proba(input)

    # Tampilkan Input
    st.write("**Input :**")
    df = pd.DataFrame(input, columns=['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)', 'Cloud Cover', 'Atmospheric Pressure', 'UV Index', 'Season', 'Visibility (km)', 'Location'])
    st.dataframe(df)

    # Tampilkan Hasil
    if predict.any():
        st.write("Presentase 4 Weather: ")

        df = pd.DataFrame(predict, index = ["result"], columns=Weather)
        st.dataframe(df)
        result = Weather[np.argmax(predict)]
        st.write("Hasil Prediksi : " + result)
        st.image(Image[np.argmax(predict)])

if __name__ == "__main__":
    main()
    
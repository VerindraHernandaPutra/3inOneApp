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
    Temperature = st.sidebar.slider("Temperature", X.Temperature.min(), X.Temperature.max(), X.Temperature.mean())
    
    # Kelembaban
    Humidity = st.sidebar.slider("Kelembaban", X.Humidity.min(), X.Humidity.max(), int(X.Humidity.mean()))

    # Kecepatan Angin
    Wind_Speed = st.sidebar.slider("Kecepatan Angin", X['Wind Speed'].min(), X['Wind Speed'].max(), X['Wind Speed'].mean())
    
    # Pengendapan (%)
    Precipitation = st.sidebar.slider("Pengendapan (%)", X['Precipitation (%)'].min(), X['Precipitation (%)'].max(), X['Precipitation (%)'].mean())
    
    # Kondisi langit
    Cloud_Cover = st.sidebar.selectbox(
        "Kondisi langit",
        ('clear', 'partly cloudy', 'cloudy', 'overcast'),
        index=None,
        placeholder="Silahkan pilih..",
    )
    Cloud_Cover = function.pilih_Cloud_Cover(Cloud_Cover)

    # Tekanan Atmosfer
    Atmospheric_Pressure = st.sidebar.slider("Tekanan Atmosfer", X['Atmospheric Pressure'].min(), X['Atmospheric Pressure'].max(), X['Atmospheric Pressure'].mean())
    
    # Indeks UV
    UV_index = st.sidebar.slider("Indeks UV", X['UV Index'].min(), X['UV Index'].max(), int(X['UV Index'].mean()))
    
    # Musim
    Season = st.sidebar.selectbox(
        "Musim",
        ('Spring', 'Summer', 'Autumn', 'Winter'),
        index=None,
        placeholder="Silahkan pilih..",
    )
    Season = function.pilih_Season(Season)

    # Jarak pandang (km)
    Visibility = st.sidebar.slider("Jarak pandang (km)", X['Visibility (km)'].min(), X['Visibility (km)'].max(), X['Visibility (km)'].mean())

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
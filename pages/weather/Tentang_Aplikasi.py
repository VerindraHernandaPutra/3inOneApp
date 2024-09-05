import streamlit as st
import pandas as pd

# Ambil Dataset hasil modifikasi
dataset = pd.read_csv("Dataset/weather_classification_data.csv")

def main():
    st.image("Asset/Weather.jpg", caption="Gambar Weather")

    st.title('📟 Tentang Aplikasi')
    st.write("Merupakan aplikasi sederhana yang dirancang menggunakan STREAMLIT dan dibangun secara hati-hati menggunakan keenam Indra pencipta.")
    st.write("\nAplikasi dirancang untuk bisa memprediksi seakurat mungkin cuaca yang akan terjadi berdasarkan data-data yang diberikan pengguna.")

    st.title('📊 Tentang Dataset')
    st.write("Kumpulan data ini dibuat secara sintetis untuk meniru data cuaca untuk tugas klasifikasi. Ini mencakup berbagai fitur terkait cuaca dan mengkategorikan cuaca menjadi empat jenis: Hujan, Cerah, Berawan, dan Bersalju. Dataset ini dirancang untuk mempraktikkan algoritma klasifikasi, prapemrosesan data, dan metode deteksi outlier")
    st.dataframe(dataset)
    st.write("Total Kolom = ", dataset.shape[0])
    st.write("Total Baris = ", dataset.shape[1])

    # Fitur
    st.write("Fitur = ")
    st.write("- **Temperature (numeric)**: The temperature in degrees Celsius, ranging from extreme cold to extreme heat.")
    st.write("- **Humidity (numeric)**: The humidity percentage, including values above 100% to introduce outliers.")
    st.write("- **Wind Speed (numeric)**: The wind speed in kilometers per hour, with a range including unrealistically high values.")
    st.write("- **Precipitation (%) (numeric)**: The precipitation percentage, including outlier values.")
    st.write("- **Cloud Cover (categorical)**: The cloud cover description.")
    st.write("- **Atmospheric Pressure (numeric)**: The atmospheric pressure in hPa, covering a wide range.")
    st.write("- **UV Index (numeric)**: The UV index, indicating the strength of ultraviolet radiation.")
    st.write("- **Season (categorical)**: The season during which the data was recorded.")
    st.write("- **Visibility (km) (numeric)**: The visibility in kilometers, including very low or very high values.")
    st.write("- **Location (categorical)**: The type of location where the data was recorded.")
    st.write("- **Weather Type (categorical)**: The target variable for classification, indicating the weather type.")

if __name__ == "__main__":
    main()
    
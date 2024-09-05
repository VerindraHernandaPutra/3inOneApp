import streamlit as st
from streamlit_option_menu import option_menu
import pages.weather.Tentang_Aplikasi as info
import pages.weather.Pred as classification_app
import pages.weather.Advance_Pred as adv_classification_app
import pages.weather.Visualisasi as visualisasi
import Function as universal_func
import pickle

with open("weather.pkl", "rb") as model_file:
    model = pickle.load(model_file)

universal_func.logo()

def main():
    st.title("🍃 Weather Classification 🍃")
    st.write("Aplikasi Sederhana berbasis Klasifikasi menggunakan Dataset Weather")
    run()

def run():

        # Sidebar
        with st.sidebar:
            selected = option_menu("APP TOOLS", ["Tentang Aplikasi", "Prediksi", "Prediksi Spesifik", "Visualisasi Data"], 
            icons=['info-circle-fill', 'bi-wrench-adjustable-circle', 'bi-wrench-adjustable-circle-fill', 'reception-4'], menu_icon="hammer", default_index=0)
        
        if selected == "Tentang Aplikasi":
             info.main()
        if selected == "Prediksi":
             classification_app.main()
        if selected == "Prediksi Spesifik":
             adv_classification_app.main()
        if selected == "Visualisasi Data":
             visualisasi.main()
             

if __name__ == "__main__":
    main()
    
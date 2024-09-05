import streamlit as st
from streamlit_option_menu import option_menu
import pages.fossil.Tentang_Aplikasi as info
import pages.fossil.Pred as regression_app
import pages.fossil.Advance_Pred as adv_regression_app
import pages.fossil.Visualisasi as visualisasi
import Function as universal_func
import pickle

with open("fossil.pkl", "rb") as model_file:
    model = pickle.load(model_file)
    
universal_func.logo()

def main():
    st.title("🦴 Age of Fossil Regression 🦴")
    st.write("Aplikasi Sederhana berbasis Regresi menggunakan Dataset Age of Fossil")
    run()

def run():

        # Sidebar
        with st.sidebar:
            selected = option_menu("APP TOOLS", ["Tentang Aplikasi", "Prediksi", "Prediksi Spesifik", "Visualisasi Data"], 
            icons=['info-circle-fill', 'bi-wrench-adjustable-circle', 'bi-wrench-adjustable-circle-fill', 'reception-4'], menu_icon="hammer", default_index=0)
        
        if selected == "Tentang Aplikasi":
             info.main()
        if selected == "Prediksi":
             regression_app.main()
        if selected == "Prediksi Spesifik":
             adv_regression_app.main()
        if selected == "Visualisasi Data":
             visualisasi.main()
             

if __name__ == "__main__":
    main()
    
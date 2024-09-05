import streamlit as st
from streamlit_option_menu import option_menu
import pages.creditcard.Tentang_Aplikasi as info
import pages.creditcard.Pred as clustering_app
import pages.creditcard.Pred_3D as clustering3D_app
import pages.creditcard.Visualisasi as visualisasi
import Function as universal_func
import pickle

with open("creditcard.pkl", "rb") as model_file:
    model = pickle.load(model_file)

universal_func.logo()

def main():
    st.title("💳 Credit Card Clustering 💳")
    st.write("Aplikasi Sederhana berbasis Clustering menggunakan Dataset Credit Card")
    run()

def run():

        # Sidebar
        with st.sidebar:
            selected = option_menu("APP TOOLS", ["Tentang Aplikasi", "Clustering", "Clustering 3D", "Visualisasi Data"], 
            icons=['info-circle-fill', 'bi-wrench-adjustable-circle', 'bi-wrench-adjustable-circle-fill', 'reception-4'], menu_icon="hammer", default_index=0)
        
        if selected == "Tentang Aplikasi":
             info.main()
        if selected == "Clustering":
             clustering_app.main()
        if selected == "Clustering 3D":
             clustering3D_app.main()
        if selected == "Visualisasi Data":
             visualisasi.main()

if __name__ == "__main__":
    main()
    
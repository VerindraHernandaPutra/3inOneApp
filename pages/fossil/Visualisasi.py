import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ambil Dataset hasil modifikasi
dataset_ori = pd.read_csv("Dataset/Age _Fossil.csv")
dataset_mod = pd.read_csv("Dataset_Final/Age _Fossil_modified.csv")

def distribusi_age():

    # Data Age
    age_ori = dataset_ori['age']

    # Data Age
    age_mod = dataset_mod['age']

    # Buat 2 kolom
    col1, col2 = st.columns(2)

    # Histogram 1
    with col1:
        fig, ax = plt.subplots()
        ax.hist(age_ori, bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frekuensi')
        ax.set_title('Distribusi Age - Dataset Original')
        st.pyplot(fig)

    # Histogram 2
    with col2:
        fig, ax = plt.subplots()
        ax.hist(age_mod, bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frekuensi')
        ax.set_title('Distribusi Age - Dataset Modified')
        st.pyplot(fig)

def main():
    st.title("Modified Dataset")
    st.dataframe(dataset_mod)
    st.write("Disini telah dilakukan beberapa modifikasi untuk meningkatkan akurasi aplikasi, salah satunya adalah pada kolom Age. Dimana saya melakukan min-max scaling untuk memudahkan model dalam memprediksi model")

    st.title("Visualisasi")

    # Histogram distribusi Age
    st.header("Distribusi Umur Fossil")
    distribusi_age()

    # Distribusi Umur Fossil berdasarkan Jenis bebatuan yang mengelilingi
    st.header("Jenis bebatuan yang mengelilingi")
    st.bar_chart(dataset_ori, x="surrounding_rock_type", y="age", stack=False)

    st.write("\nTo be Continued...")

if __name__ == "__main__":
    main()
    
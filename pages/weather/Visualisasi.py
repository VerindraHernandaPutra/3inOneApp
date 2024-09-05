import streamlit as st
import pandas as pd

# Ambil Dataset hasil modifikasi
dataset_ori = pd.read_csv("Dataset/weather_classification_data.csv")
dataset_mod = pd.read_csv("Dataset_Final/weather_modified.csv")

def main():
    st.title("Modified Dataset")
    st.dataframe(dataset_mod)

    st.title("Visualisasi")

    # Histogram distribusi Age
    st.header("Distribusi Weather berdasarkan Temperature")
    st.bar_chart(dataset_ori, x="Weather Type", y="Temperature", stack=False)

    st.write("\nTo be Continued...")

if __name__ == "__main__":
    main()
    
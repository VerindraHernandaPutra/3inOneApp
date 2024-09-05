import streamlit as st
import pandas as pd

# Ambil Dataset hasil modifikasi
dataset_ori = pd.read_csv("Dataset/CC GENERAL.csv")
dataset_mod = pd.read_csv("Dataset_Final/CC_GENERAL_modified.csv")

def main():
    st.title("Modified Dataset")
    st.dataframe(dataset_mod)

    st.title("Visualisasi")

    # Histogram distribusi
    st.header("Distribusi PAYMENTS berdasarkan MINIMUM_PAYMENTS")
    st.bar_chart(dataset_mod, x="PAYMENTS", y="MINIMUM_PAYMENTS", stack=False)

    st.write("\nTo be Continued...")

if __name__ == "__main__":
    main()
    
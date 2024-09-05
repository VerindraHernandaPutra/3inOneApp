import streamlit as st
import pages.creditcard.Function as function
import pandas as pd

# Ambil Dataset hasil modifikasi
dataset = pd.read_csv("Dataset_Final/CC_GENERAL_modified.csv")
dataset_ori = dataset

def main():
    st.sidebar.title('Input')

    # Temperature
    nCluster = st.sidebar.slider("Jumlah Kluster", 1, 10, 1)

    # Input Kolom 1
    kolom_1 = st.sidebar.selectbox(
        "Pilih Kolom 1",
        ("BALANCE", "BALANCE_FREQUENCY", "PURCHASES", 'ONEOFF_PURCHASES',
       'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY',
       'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY',
       'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX',
       'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT',
       'TENURE'),
        index=0,
        placeholder="Silahkan pilih..",
    )

    # Input Kolom 2
    kolom_2 = st.sidebar.selectbox(
        "Pilih Kolom 2",
        ("BALANCE", "BALANCE_FREQUENCY", "PURCHASES", 'ONEOFF_PURCHASES',
       'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY',
       'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY',
       'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX',
       'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT',
       'TENURE'),
        index=None,
        placeholder="Silahkan pilih..",
    )

    # Input Kolom 3
    kolom_3 = st.sidebar.selectbox(
        "Pilih Kolom 3",
        ("BALANCE", "BALANCE_FREQUENCY", "PURCHASES", 'ONEOFF_PURCHASES',
       'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY',
       'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY',
       'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX',
       'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT',
       'TENURE'),
        index=None,
        placeholder="Silahkan pilih..",
    )

    # Tampilkan Dataset Ori
    st.write("**Dataset Sebelum Clustering :**")
    st.dataframe(dataset_ori)

    # Tampilkan elbow method
    st.write("**Elbow Method untuk melihat cluster optimal :**")
    function.elbow_method(dataset)

    #autoKmeans3D
    function.autoKmeans3D(kolom_1, kolom_2, kolom_3, nCluster, dataset)
    

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd

# Ambil Dataset hasil modifikasi
dataset = pd.read_csv("Dataset/CC GENERAL.csv")

def main():
    st.image("Asset/CreditCard.jpg", caption="Gambar CreditCard")

    st.title('📟 Tentang Aplikasi')
    st.write("Merupakan aplikasi sederhana yang dirancang menggunakan STREAMLIT dan dibangun secara hati-hati menggunakan keenam Indra pencipta.")
    st.write("\nAplikasi dirancang untuk memberikan informasi dengan cara clustering.")

    st.title('📊 Tentang Dataset')
    st.write("Hal ini memerlukan pengembangan segmentasi pelanggan untuk menentukan strategi pemasaran. Contoh Kumpulan Data merangkum perilaku penggunaan sekitar 9000 pemegang kartu kredit aktif selama 6 bulan terakhir. File tersebut berada di tingkat pelanggan dengan 18 variabel perilaku.")
    st.dataframe(dataset)
    st.write("Total Kolom = ", dataset.shape[0])
    st.write("Total Baris = ", dataset.shape[1])

    # Fitur
    st.write("Fitur = ")
    st.write("- **CUST_ID** : Identification of Credit Card holder (Categorical)")
    st.write("- **BALANCE** : Balance amount left in their account to make purchases")
    st.write("- **BALANCE_FREQUENCY** : How frequently the Balance is updated, score between 0 and 1 (1 = frequently updated, 0 = not frequently updated)")
    st.write("- **PURCHASES** : Amount of purchases made from account")
    st.write("- **ONEOFF_PURCHASES** : Maximum purchase amount done in one-go")
    st.write("- **INSTALLMENTS_PURCHASES** : Amount of purchase done in installment")
    st.write("- **CASH_ADVANCE** : Cash in advance given by the user")
    st.write("- **PURCHASES_FREQUENCY** : How frequently the Purchases are being made, score between 0 and 1 (1 = frequently purchased, 0 = not frequently purchased)")
    st.write("- **ONEOFFPURCHASESFREQUENCY** : How frequently Purchases are happening in one-go (1 = frequently purchased, 0 = not frequently purchased)")
    st.write("- **PURCHASESINSTALLMENTSFREQUENCY** : How frequently purchases in installments are being done (1 = frequently done, 0 = not frequently done)")
    st.write("- **CASHADVANCEFREQUENCY** : How frequently the cash in advance being paid")
    st.write("- **CASHADVANCETRX** : Number of Transactions made with Cash in Advanced")
    st.write("- **PURCHASES_TRX** : Numbe of purchase transactions made")
    st.write("- **CREDIT_LIMIT** : Limit of Credit Card for user")
    st.write("- **PAYMENTS** : Amount of Payment done by user")
    st.write("- **MINIMUM_PAYMENTS** : Minimum amount of payments made by user")
    st.write("- **PRCFULLPAYMENT** : Percent of full payment paid by user")
    st.write("- **TENURE** : Tenure of credit card service for user")

if __name__ == "__main__":
    main()
    
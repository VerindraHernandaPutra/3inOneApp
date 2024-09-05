import streamlit as st
import pandas as pd

# Ambil Dataset hasil modifikasi
dataset = pd.read_csv("Dataset/Age _Fossil.csv")

def main():
    st.image("Asset/Fossil.jpg", caption="Gambar Fossil")

    st.title('📟 Tentang Aplikasi')
    st.write("Merupakan aplikasi sederhana yang dirancang menggunakan STREAMLIT dan dibangun secara hati-hati menggunakan keenam Indra pencipta.")
    st.write("\nAplikasi dirancang untuk bisa memprediksi seakurat mungkin umur dari sebuah fossil berdasarkan data-data yang diberikan pengguna.")

    st.title('📊 Tentang Dataset')
    st.write("Kumpulan data Fosil dibuat untuk memberikan landasan yang komprehensif dan realistis untuk melatih dan mengevaluasi model pembelajaran mesin yang bertujuan memprediksi usia fosil. Kumpulan data ini memiliki tingkat kesulitan menengah dan mencakup berbagai atribut geologi, kimia, dan fisik yang penting dalam studi pembentukan dan pelestarian fosil.")
    st.write("\nData awal sebagian besar bersumber dari PaleoBioDB, dengan tambahan sumber swasta yang berkontribusi pada kumpulan data tersebut. Setelah membuat kumpulan data awal yang kecil, model pembelajaran mendalam digunakan untuk memperluas dan menghasilkan versi sintetis. Kumpulan data sintetik ini menyimulasikan skenario realistis, menjadikannya alat yang berharga bagi ilmuwan data dan peneliti di lapangan.")
    st.dataframe(dataset)
    st.write("Total Kolom = ", dataset.shape[0])
    st.write("Total Baris = ", dataset.shape[1])

    # Fitur
    st.write("Fitur = ")
    st.write("- **uranium_lead_ratio**: Ratio of uranium to lead isotopes in the fossil sample.")
    st.write("- **carbon_14_ratio**: Ratio of carbon-14 isotopes present in the fossil sample.")
    st.write("- **radioactive_decay_series**: Measurement of the decay series from parent to daughter isotopes.")
    st.write("- **stratigraphic_layer_depth**: Depth of the fossil within the stratigraphic layer, in meters.")
    st.write("- **isotopic_composition**: Proportion of different isotopes within the fossil sample.")
    st.write("- **fossil_size**: Size of the fossil, in centimeters.")
    st.write("- **fossil_weight**: Weight of the fossil, in grams.")
    st.write("- **geological_period**: Geological period during which the fossil was formed.")
    st.write("- **surrounding_rock_type**: Type of rock surrounding the fossil.")
    st.write("- **paleomagnetic_data**: Paleomagnetic orientation data of the fossil site.")
    st.write("- **stratigraphic_position**: Position of the fossil within the stratigraphic column.")
    st.write("- **age**: Calculated age of the fossil based on various features, in years.")

if __name__ == "__main__":
    main()
    
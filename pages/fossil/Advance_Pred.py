import streamlit as st
import pages.fossil.Function as function
import pickle
import numpy as np
import pandas as pd

with open("fossil.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def main():
    st.sidebar.title('Input')

    # Uranium
    uranium_lead_ratio = st.sidebar.text_input("Rasio Uranium", placeholder="Silahkan masukkan angka..")
    uranium_lead_ratio = function.handle_empty_input(uranium_lead_ratio)

    # Rasio Isotop Karbon-14
    carbon_14_ratio = st.sidebar.text_input("Rasio Isotop Karbon-14", placeholder="Silahkan masukkan angka..")
    carbon_14_ratio = function.handle_empty_input(carbon_14_ratio)

    # Pengukuran Seri Pembusukan
    radioactive_decay_series = st.sidebar.text_input("Pengukuran Seri Pembusukan", placeholder="Silahkan masukkan angka..")
    radioactive_decay_series = function.handle_empty_input(radioactive_decay_series)

    # Kedalaman Fosil (Lapisan Stratigrafi)
    stratigraphic_layer_depth = st.sidebar.text_input("Kedalaman Fosil (Lapisan Stratigrafi)", placeholder="Silahkan masukkan angka..")
    stratigraphic_layer_depth = function.handle_empty_input(stratigraphic_layer_depth)

    # Periode geologi
    geological_period = st.sidebar.selectbox(
        "Periode geologi",
        ("Cambrian", "Triassic", "Cretaceous", "Devonian", "Jurassic", "Paleogene", "Permian", "Neogene", "Ordovician", "Carboniferous", "Silurian"),
        index=None,
        placeholder="Silahkan pilih..",
    )
    geological_period = function.pilih_geological_period(geological_period)

    # Pilih Data Paleomagnetik
    paleomagnetic_data = st.sidebar.radio(
        "Pilih Data Paleomagnetik",
        options=["Normal polarity", "Reversed polarity"],
        index=None
    )
    paleomagnetic_data = function.pilih_paleomagnetic_data(paleomagnetic_data)

    # "Penyertaan Fosil lainnya
    inclusion_of_other_fossils = st.sidebar.radio(
        "Penyertaan Fosil lainnya",
        options=[True, False],
        index=None
    )
    inclusion_of_other_fossils = function.pilih_inclusion_of_other_fossils(inclusion_of_other_fossils)

    # Komposisi Isotopic
    isotopic_composition = st.sidebar.text_input("Komposisi Isotopic", placeholder="Silahkan masukkan angka..")
    isotopic_composition = function.handle_empty_input(isotopic_composition)

    # Jenis Bebatuan yang mengelilingi
    surrounding_rock_type = st.sidebar.selectbox(
        "Jenis Bebatuan yang mengelilingi",
        ("Sandstone", "Limestone", "Shale", "Conglomerate"),
        index=None,
        placeholder="Silahkan pilih..",
    )
    surrounding_rock_type = function.pilih_surrounding_rock_type(surrounding_rock_type)

    # Posisi Stratigraphic
    stratigraphic_position = st.sidebar.selectbox(
        "Posisi Stratigraphic",
        ("Bottom", "Middle", "Top"),
        index=None,
        placeholder="Silahkan pilih..",
    )
    stratigraphic_position = function.pilih_stratigraphic_position(stratigraphic_position)

    # Ukuran Fossil
    fossil_size = st.sidebar.text_input("Ukuran Fossil", placeholder="Silahkan masukkan angka..")
    fossil_size = function.handle_empty_input(fossil_size)

    # Berat Fossil
    fossil_weight = st.sidebar.text_input("Berat Fossil", placeholder="Silahkan masukkan angka..")
    fossil_weight = function.handle_empty_input(fossil_weight)

    # Prediksi
    input = np.array([uranium_lead_ratio, carbon_14_ratio, radioactive_decay_series, stratigraphic_layer_depth, geological_period, paleomagnetic_data, inclusion_of_other_fossils, isotopic_composition, surrounding_rock_type, stratigraphic_position, fossil_size, fossil_weight])
    input = np.expand_dims(input, axis = 0)
    predict = model.predict(input)

    # Mengembalikan ke bentuk asli
    min_age = 4208
    max_age = 103079
    predict = predict * (max_age - min_age) + min_age

    # Tampilkan Input
    st.write("**Input :**")
    df = pd.DataFrame(input, columns=['uranium_lead_ratio', 'carbon_14_ratio', 'radioactive_decay_series', 'stratigraphic_layer_depth', 'geological_period', 'paleomagnetic_data', 'inclusion_of_other_fossils', 'isotopic_composition', 'surrounding_rock_type', 'stratigraphic_position', 'fossil_size', 'fossil_weight'])
    st.dataframe(df)

    # Tampilkan Hasil
    if predict.any():
        st.write("**Hasil Prediksi :**")
        st.success("Umur Fossil = {} Tahun".format(int(predict)))

if __name__ == "__main__":
    main()
    
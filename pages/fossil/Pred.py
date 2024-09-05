import streamlit as st
import pages.fossil.Function as function
import pickle
import numpy as np
import pandas as pd

with open("fossil.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def main():
    st.sidebar.title('Input')
    uranium_lead_ratio = st.sidebar.slider("Rasio Uranium", 0.0, 1.2, 0.6)

    carbon_14_ratio = st.sidebar.slider("Rasio Isotop Karbon-14", 0.0, 1.0, 0.5)

    radioactive_decay_series = st.sidebar.slider("Pengukuran Seri Pembusukan", 0.0, 1.33, 0.66)

    stratigraphic_layer_depth = st.sidebar.slider("Kedalaman Fosil (Lapisan Stratigrafi)", 0.0, 401.75, 200.87)

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

    isotopic_composition = st.sidebar.slider("Komposisi Isotopic", 0.0, 2.42, 1.26)

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
    
    # Besar Fossil
    fossil_size = st.sidebar.slider("Ukuran Fossil", 0.0, 177.36, 88.68)
    
    # Berat Fossil
    fossil_weight = st.sidebar.slider("Berat Fossil", 0.0, 867.22, 438.66)

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

    if predict.any():
        st.write("**Hasil Prediksi :**")
        st.success("Hasil Prediksi Umur Fosil = {} Tahun".format(int(predict)))

if __name__ == "__main__":
    main()
    
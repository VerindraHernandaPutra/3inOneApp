import streamlit as st

# Fungsi untuk mengatasi input kosong
def handle_empty_input(input_value):
  try:
    return float(input_value) if input_value else 0
  except ValueError:
    st.error("Masukkan harus berupa angka.")
    return 0

# Fungsi Untuk Memilih geological_period
def pilih_geological_period(geological_period):
    if geological_period == "Cambrian":
        geological_period = 0
    elif geological_period == "Triassic":
        geological_period = 10
    elif geological_period == "Cretaceous":
        geological_period = 2
    elif geological_period == "Devonian":
        geological_period = 3
    elif geological_period == "Jurassic":
        geological_period = 4 
    elif geological_period == "Paleogene":
        geological_period = 7
    elif geological_period == "Permian":
        geological_period = 8
    elif geological_period == "Neogene":
        geological_period = 5
    elif geological_period == "Ordovician":
        geological_period = 6
    elif geological_period == "Carboniferous":
        geological_period = 1
    elif geological_period == "Silurian":
        geological_period = 9
    
    # Handle Empty Value
    geological_period = handle_empty_input(geological_period)

    return geological_period

# Fungsi Untuk Memilih paleomagnetic_data
def pilih_paleomagnetic_data(paleomagnetic_data):
    if paleomagnetic_data == "Normal polarity":
        paleomagnetic_data = 0
    elif paleomagnetic_data == "Reversed polarity":
        paleomagnetic_data = 1

    # Handle Empty Value
    paleomagnetic_data = handle_empty_input(paleomagnetic_data)
        
    return paleomagnetic_data

# Fungsi Untuk Memilih inclusion_of_other_fossils
def pilih_inclusion_of_other_fossils(inclusion_of_other_fossils):
    if inclusion_of_other_fossils == True:
        inclusion_of_other_fossils = 1
    elif inclusion_of_other_fossils == False:
        inclusion_of_other_fossils = 0

    # Handle Empty Value
    inclusion_of_other_fossils = handle_empty_input(inclusion_of_other_fossils)
        
    return inclusion_of_other_fossils

# Fungsi Untuk Memilih surrounding_rock_type
def pilih_surrounding_rock_type(surrounding_rock_type):
    if surrounding_rock_type == "Sandstone":
        surrounding_rock_type = 2
    elif surrounding_rock_type == "Limestone":
        surrounding_rock_type = 1
    elif surrounding_rock_type == "Shale":
        surrounding_rock_type = 3
    elif surrounding_rock_type == "Conglomerate":
        surrounding_rock_type = 0

    # Handle Empty Value
    surrounding_rock_type = handle_empty_input(surrounding_rock_type)
        
    return surrounding_rock_type

# Fungsi Untuk Memilih surrounding_rock_type
def pilih_surrounding_rock_type(surrounding_rock_type):
    if surrounding_rock_type == "Sandstone":
        surrounding_rock_type = 2
    elif surrounding_rock_type == "Limestone":
        surrounding_rock_type = 1
    elif surrounding_rock_type == "Shale":
        surrounding_rock_type = 3
    elif surrounding_rock_type == "Conglomerate":
        surrounding_rock_type = 0

    # Handle Empty Value
    surrounding_rock_type = handle_empty_input(surrounding_rock_type)
        
    return surrounding_rock_type

# Fungsi Untuk Memilih stratigraphic_position
def pilih_stratigraphic_position(stratigraphic_position):
    if stratigraphic_position == "Bottom":
        stratigraphic_position = 0
    elif stratigraphic_position == "Middle":
        stratigraphic_position = 1
    elif stratigraphic_position == "Top":
        stratigraphic_position = 2

    # Handle Empty Value
    stratigraphic_position = handle_empty_input(stratigraphic_position)
        
    return stratigraphic_position

import streamlit as st

# Fungsi untuk mengatasi input kosong
def handle_empty_input(input_value):
  try:
    return float(input_value) if input_value else 0
  except ValueError:
    st.error("Masukkan harus berupa angka.")
    return 0

# Fungsi Untuk Memilih Cloud_Cover
def pilih_Cloud_Cover(Cloud_Cover):
    if Cloud_Cover == 'clear':
        Cloud_Cover = 0
    elif Cloud_Cover == 'partly cloudy':
        Cloud_Cover = 1
    elif Cloud_Cover == 'cloudy':
        Cloud_Cover = 2
    elif Cloud_Cover == 'overcast':
        Cloud_Cover = 3
    
    # Handle Empty Value
    Cloud_Cover = handle_empty_input(Cloud_Cover)

    return Cloud_Cover

# Fungsi Untuk Memilih Season
def pilih_Season(Season):
    if Season == 'Spring':
        Season = 0
    elif Season == 'Summer':
        Season = 1
    elif Season == 'Autumn':
        Season = 2
    elif Season == 'Winter':
        Season = 3

    # Handle Empty Value
    Season = handle_empty_input(Season)
        
    return Season

# Fungsi Untuk Memilih Location
def pilih_Location(Location):
    if Location == 'Coastal':
        Location = 0
    elif Location == 'Inland':
        Location = 1
    elif Location == 'Mountain':
        Location = 2

    # Handle Empty Value
    Location = handle_empty_input(Location)
        
    return Location



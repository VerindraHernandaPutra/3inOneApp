import streamlit as st
from st_clickable_images import clickable_images
import base64

def logo():
    LOGO = "Asset/Logo.png"
    NAMA = "Asset/VERINDRA.png"
    st.logo(NAMA, icon_image = LOGO)

# Fungsi Pilih Page
def pilih_page():
    images = []
    for file in ["Asset/Page1.png", "Asset/Page2.png", "Asset/Page3.png"]:
        with open(file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images.append(f"data:image/png;base64,{encoded}")

    clicked = clickable_images(
    images,
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "10px", "height": "300px"},
    )
    if clicked == 0:
        st.switch_page("pages/2_🦴_Prediksi_Umur_Fossil.py")
    if clicked == 1:
        st.switch_page("pages/3_👳_Prediksi_Cuaca.py")
    if clicked == 2:
        st.switch_page("pages/4_💳_Credit_Card.py")



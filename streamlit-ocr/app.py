import streamlit as st
from PIL import Image
import pytesseract
import os

st.title("OCR con PyTesseract")
st.write("Sube una imagen y extraeremos el texto con OCR.")

uploaded_file = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_column_width=True)

    if st.button("Extraer texto"):
        text = pytesseract.image_to_string(image)
        st.subheader("Texto extraído:")
        st.text(text)
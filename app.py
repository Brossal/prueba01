import streamlit as st 
import os

def salida(text:str):
    lista = text.split(" ")
    for x in lista:
        st.write(x)


respuesta = st.text_input("Escribe cualquier cosa.")
if st.button("Enviar"):
    salida(respuesta)
if st.button("listdir"):
    st.write(os.listdir())
data = st.file_uploader("cargar")

import streamlit as st 


def salida(text:str):
    lista = text.split(" ")
    for x in lista:
        st.write(x)


respuesta = st.text_input("Escribe cualquier cosa.")
if st.button("Enviar"):
    salida(respuesta)


data = st.upload_file("cargar")

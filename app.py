import streamlit as st 


def salida(text:str):
    lista = text.split(" ")
    for x in lista:
        st.write(x)


if st.button("Enviar"):
    salida("hola mundo")

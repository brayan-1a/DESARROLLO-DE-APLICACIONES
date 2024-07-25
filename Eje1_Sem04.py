import streamlit as st
import pandas as pd 

#Título de la aplicación
st.title("Análisis de Ventas")

#Subir el archivo Excel
archivo = st.file_uploader("Cargar Archivo Excel", type=["xlsx"])

if archivo is not None:
    #Leer el archivo Excel
    df = pd.read_excel(archivo)
    st.write("Datos Cargados:")
    st.write(df)
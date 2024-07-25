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
    
    #Calcular el total de ventas por producto usando un bucle For
    st.header("Total de Ventas por Producto")
    total_ventas = {}
    for index, row in df.iterrows():
        producto = row['Producto']
        total = row['Cantidad'] * row['Precio']
        if producto in total_ventas:
            total_ventas[producto] += total
        else:
            total_ventas[producto] = total
            
    st.write(total_ventas)

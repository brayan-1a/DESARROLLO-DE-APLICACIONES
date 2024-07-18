import streamlit as st
import pandas as pd

#Titulo de aplicación
st.title("Cargar y Procesar Archivo Excel con Condicionales")

#Subir el archivo Excel
archivo = st.file_uploader("Cargar Archivo Excel", type=["xlsx"])

if archivo is not None:

    #Leer el archivo Excel
    df = pd.read_excel(archivo)
    st.write("Datos cargados:")
    st.write(df)

    #Función para clasificar edades
    def clasificar_edad(edad):
        if edad < 18:
            return "Menor Edad"
        elif 18 <= edad < 65:
            return "Adulto"
        else:
            return "Adulto Mayor"

    #Aplicar la función a la columna Edad    
    df["Clasificación"] = df["Edad"].apply(clasificar_edad)

    #Mostrar ek dataframe con la calsificación
    st.write("Datos Clasificados:")
    st.write(df)

    #Guardar el dataframe modificado a un nuevo archivo Excel
    df.to_excel("datos_clasificados.xlsx", index=False)
    st.success("Archivo procesado y guardado como datos_clasificados.xlsx")   
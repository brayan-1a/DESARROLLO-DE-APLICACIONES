import streamlit as st
import pandas as pd
import os

# Título de la aplicación
st.title("Cargar y Procesar Archivo Excel con Condicionales")

# Subir el archivo Excel
archivo = st.file_uploader("Cargar Archivo Excel", type=["xlsx"])

if archivo is not None:
    # Leer el archivo Excel
    df = pd.read_excel(archivo)
    st.write("Datos cargados:")
    st.write(df)

    # Función para clasificar edades
    def clasificar_edad(edad):
        if edad < 18:
            return "Menor Edad"
        elif 18 <= edad < 65:
            return "Adulto"
        else:
            return "Adulto Mayor"

    # Aplicar la función a la columna Edad
    df["Clasificación"] = df["Edad"].apply(clasificar_edad)

    # Mostrar el dataframe con la clasificación
    st.write("Datos Clasificados:")
    st.write(df)

    # Especificar la ruta donde se guardará el archivo modificado
    save_path = r"C:\Users\ADMIN\Downloads\modificaciones\datos_clasificados.xlsx"

    # Crear el directorio si no existe
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Guardar el dataframe modificado a un nuevo archivo Excel
    df.to_excel(save_path, index=False)
    st.success(f"Archivo procesado y guardado en {save_path}")

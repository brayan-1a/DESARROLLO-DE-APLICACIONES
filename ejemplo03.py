import streamlit as st
import pandas as pd
import io

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

    # Guardar el dataframe modificado a un nuevo archivo Excel en un buffer de memoria
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)

    # Mostrar mensaje de éxito
    st.success("Archivo procesado y listo para descargar.")

    # Proporcionar un enlace para descargar el archivo guardado
    st.download_button(
        label="Descargar archivo procesado",
        data=buffer,
        file_name="datos_clasificados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


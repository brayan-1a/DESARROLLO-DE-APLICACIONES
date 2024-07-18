import streamlit as st
import pandas as pd

st.title("Cargar y Procesar Archivo Excel con Condicionales")

# Especifica la ruta completa al archivo
ruta_archivo = "C:/Users/ADMIN/Downloads/datos.xlsx"

# Verifica si el archivo existe
if st.file_uploader is not None:

    #Leer el archivo Excel
    df = pd.read_excel(ruta_archivo)
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

    #Mostrar el dataframe con la clasificación
    st.write("Datos Clasificados:")
    st.write(df)

    #Guardar el dataframe modificado a un nuevo archivo Excel
    df.to_excel("datos_clasificados.xlsx", index=False)
    st.success("Archivo procesado y guardado como datos_clasificados.xlsx")
else:
    st.warning("Por favor, carga un archivo Excel.")
 
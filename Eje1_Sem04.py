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

     #Mostrar el resultado de una tarea repetitiva usando un bucle While
    st.header("Tarea Repetitiva con While")
    contador = 0
    resultado = []
    while contador < 5:
        resultado.append(f"Tarea repetitiva {contador + 1}")
        contador += 1

    st.write(resultado)

    #Guardar el resultado en un nuevo archivo CSV
    resultado_df = pd.DataFrame(list(total_ventas.items()), columns=['Producto', 'Total Ventas'])
    
    #convertir DataFrame a CSV
    csv = resultado_df.to_csv(index=False).encode('utf-8')

    #Mensaje de éxito
    st.success("Archivo procesado")

    #botón
    st.download_button(
        label="Descargar archivo CSV",
        data=csv,
        file_name='Total_ventas.csv',
        mime='text/csv'
    )

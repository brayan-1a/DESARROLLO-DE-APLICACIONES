import streamlit as st
import pandas as pd

# Definir las categorías válidas
categorias_validas = ["Alimentos Procesados", "Condimentos", "Lácteos", "Bebidas", "Verduras",
    "Ingredientes de Cocina", "Desayunos"]

# Crear un DataFrame vacío para almacenar productos agregados
productos_agregados_df = pd.DataFrame(columns=['Nombre del producto', 'Precio del producto', 'Categorías del producto', 'En venta'])

# Título de la aplicación
st.title("Formulario de Productos - Confitería Dulcino")

# Cargar el archivo Excel
archivo = st.file_uploader("Cargar Archivo Excel", type=["xlsx"])

if archivo is not None:
    df = pd.read_excel(archivo)
    st.write("Datos Cargados:")
    st.write(df)
    
    # Procesar el archivo Excel
    for index, row in df.iterrows():
        nombre = row['Nombre del producto']
        precio = row['Precio del producto']
        categorias = row['Categorías del producto']
        en_venta = row['En venta']

        # Validaciones
        if len(nombre) > 20:
            st.error(f"Error en el producto {nombre}: El nombre del producto no debe ser mayor a 20 caracteres.")
            continue

        try:
            precio = float(precio)
            if precio <= 0 or precio >= 999:
                st.error(f"Error en el producto {nombre}: El precio del producto debe ser mayor a 0 y menor a 999 soles.")
                continue
        except ValueError:
            st.error(f"Error en el producto {nombre}: Por favor verifique el campo del precio.")
            continue

        categorias = categorias.split(",")
        for categoria in categorias:
            if categoria.strip() not in categorias_validas:
                st.error(f"Error en el producto {nombre}: La categoría {categoria} no es válida.")
                break
        else:
            # Validar el estado de venta
            if en_venta not in ["Si", "No"]:
                st.error(f"Error en el producto {nombre}: El estado del producto en venta debe ser 'Si' o 'No'.")
                continue

            # Si todas las validaciones son correctas
            st.success(f"Felicidades, su producto {nombre} se agregó correctamente.")
            # Agregar el producto al DataFrame
            productos_agregados_df = productos_agregados_df.append({
                'Nombre del producto': nombre,
                'Precio del producto': precio,
                'Categorías del producto': categorias,
                'En venta': en_venta
            }, ignore_index=True)

# Formulario de ingreso de datos
st.header("Agregar Producto")

# Controles de ingreso de datos
nombre_producto = st.text_input("Nombre del producto")
precio_producto = st.text_input("Precio del producto")
categorias_producto = st.multiselect("Categorías del producto", categorias_validas)
en_venta = st.radio("¿El producto está en venta?", ["Si", "No"])

# Botón para agregar el producto
if st.button("Agregar Producto"):
    # Validaciones
    if len(nombre_producto) > 20:
        st.error("El nombre del producto no debe ser mayor a 20 caracteres.")
    elif not precio_producto.replace('.', '', 1).isdigit():
        st.error("Por favor verifique el campo del precio.")
    else:
        precio_producto = float(precio_producto)
        if precio_producto <= 0 or precio_producto >= 999:
            st.error("El precio del producto debe ser mayor a 0 y menor a 999 soles.")
        elif not all(categoria in categorias_validas for categoria in categorias_producto):
            st.error("Una o más categorías seleccionadas no son válidas.")
        else:
            # Si todas las validaciones son correctas
            st.success("Felicidades, su producto se agregó correctamente.")
            # Agregar el producto al DataFrame
            productos_agregados_df = productos_agregados_df.append({
                'Nombre del producto': nombre_producto,
                'Precio del producto': precio_producto,
                'Categorías del producto': categorias_producto,
                'En venta': en_venta
            }, ignore_index=True)

# Mostrar los productos agregados
st.header("Productos Agregados")
if not productos_agregados_df.empty:
    st.write(productos_agregados_df)
else:
    st.write("No se han agregado productos aún.")


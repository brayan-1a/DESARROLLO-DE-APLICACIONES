import streamlit as st

#Título de la aplicación
st.title("Ingreso de Datos y Estructuras Condicionales")

#Ingreso de la edad
edad = st.number_input("Ingrese su edad", min_value=0, max_value=120, step=1)


#Función para determinar el mesaje basado en la edad
def determinar_mensaje(edad):
    if edad < 18:
        return "Eres menor de edad."
    elif 18 <= edad < 65:
        return "Eres adulto."
    else:
        return "Eres adulto mayor."

#Mostrar el Mensaje
mensaje = determinar_mensaje(edad)
st.write(mensaje)
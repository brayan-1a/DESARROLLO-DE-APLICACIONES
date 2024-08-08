import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Configurar Supabase
URL = "https://clmdobighgagqdqwfclt.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsbWRvYmlnaGdhZ3FkcXdmY2x0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI0NzMzMDYsImV4cCI6MjAzODA0OTMwNn0.7pncUo2SvBwi1Jnxl863e9-omO8fGulmZC3_zhUVFTM"
supabase: Client = create_client(URL, KEY)

st.title("sistema de facturacion")

# Selección de operación
option = st.selectbox(
    '¿Qué operación desea realizar?',
    ('Consultar Clientes', 'Consultar Productos', 'Generar Factura', 'Ver Facturas')
)

if option == 'Consultar Clientes':
    clientes = supabase.table('clientes').select('*').execute()
    df_clientes = pd.DataFrame(clientes.data)
    st.write(df_clientes)

elif option == 'Consultar Productos':
    productos = supabase.table('productos').select('*').execute()
    df_productos = pd.DataFrame(productos.data)
    st.write(df_productos)
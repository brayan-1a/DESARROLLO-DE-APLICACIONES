import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Configurar Supabase
SUPABASE_URL = "https://clmdobighgagqdqwfclt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsbWRvYmlnaGdhZ3FkcXdmY2x0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI0NzMzMDYsImV4cCI6MjAzODA0OTMwNn0.7pncUo2SvBwi1Jnxl863e9-omO8fGulmZC3_zhUVFTM"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("sistema de facturacion")
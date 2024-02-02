import streamlit as st
import numpy as np
from datetime import datetime
import pandas as pd
from pymongo import MongoClient

st.set_page_config(page_title="Portal de Suprimentos")
st.sidebar.image("logo_globo.png")
st.title("Portal de Suprimentos")
st.subheader("Página inicial")
st.write("---")
st.markdown("Bem vindo ao portal de Gestão e controles administrativos do Setor de :blue[Suprimentos!]")
st.markdown("Escolha no Menu ao lado a opção desejada.")
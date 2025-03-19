import streamlit as st
from datetime import datetime
from pymongo import MongoClient

connectString = "mongodb+srv://suprimentosdglobo:suprimentosdg2023@cluster0.dx7yrgp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connectString)
db = client["confirmations"]
mycolection = db.Cl01

st.set_page_config(page_title="Confirmação de Entrega")
col1, col2 = st.columns([6, 1])
col1.title("Portal de Suprimentos")
image_path = "logo_globo.png"
image = col2.image(image_path, width=80)
st.subheader("Confirmação de Entrega")

regions = ["Piauí", "Maranhão", "Rio Grande do Norte", "Bahia", "Pará"]
suppliers = ["Atlas Papelaria", "Atakadinho Bahia", "Autopel", "Brilhante", "Casa Norte", "Distribuidora Teresina", "JB Depósito de Construção", "J D R Sousa", "Macropack", "Mix Comércio", "Nacional", "Norte Saúde Hospitalar", "Supermercado São Jorge (JB)","Nagem","Dias Comércio","HR Papeis","Perola","Limpac"]

with st.form(key="include_confirmation", clear_on_submit=True):
    name = st.text_input("Digite seu Nome:", )
    region = st.selectbox("Selecione sua Regional:", regions)
    store = st.number_input("Digite sua Loja:", min_value=0, max_value=999)
    supplier = st.selectbox("Selecione o Fornecedor:", suppliers)
    date = st.date_input("Data do Recebimento:", format="DD/MM/YYYY")
    nf = st.number_input("N° da Nota Fiscal:", step=1, format="%d")
    send1 = st.form_submit_button("Enviar Confirmação")
    if send1:
        formatted_date = datetime.strftime(date, "%d/%m/%Y")
        current_timestamp = datetime.now().timestamp()
        formatted_timestamp = datetime.fromtimestamp(current_timestamp).strftime("%d/%m/%Y %H:%M:%S")

        if not name or not region or not store or not supplier or not date or not nf:
            st.warning("Por favor, preencha todos os campos.")
        else:
            data_to_insert = {
                'nome': name,
                'regional': region,
                'loja': store,
                'fornecedor': supplier,
                'data_recebimento': formatted_date,
                'nf': nf,
                'timestamp': formatted_timestamp
            }
            mycolection.insert_one(data_to_insert)
            st.success("Dados enviados com sucesso!")
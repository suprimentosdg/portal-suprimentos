import streamlit as st
from datetime import datetime
from pymongo import MongoClient

connectString = "mongodb+srv://suprimentosdglobo:suprimentosdg2023@cluster0.dx7yrgp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connectString)
db = client["confirmations"]
mycolection = db.Cl02

st.set_page_config(page_title="Impressoras")
col1, col2 = st.columns([6, 1])
col1.title("Portal de Suprimentos")
image_path = "logo_globo.png"
image = col2.image(image_path, width=80)
st.subheader("Abertura de Chamado para Impressora")

regions = ["Piauí", "Maranhão", "Rio Grande do Norte", "Bahia", "Pará"]

with st.form(key="include_called", clear_on_submit=True):
    name = st.text_input("Digite seu Nome:")
    region = st.selectbox("Selecione sua Regional:", regions)
    store = st.number_input("Digite sua Loja:", min_value=0, max_value=999)
    printerTypes = st.selectbox("Selecione seu modelo de Impressora:", ["BROTHER DCP 1602","BROTHER DCP 1617","BROTHER DCP 7065","BROTHER DCP 7460","BROTHER DCP 7860","BROTHER DCP 8112","BROTHER DCP 8152","BROTHER DCP 8157","BROTHER DCP 8912","BROTHER DCP L5652DN","CANON G2110","CANON G3111","HP LASER JET M125","HP LASER JET M127","HP LASER JET M225","HP LASER JET M426","HP LASER JET M428","HP LASER JET M1132","HP LASER JET M1212","HP LASER JET M1536", "PANTUM M6559 NW"])
    options = st.selectbox("Escolha uma Opção:", ["Solicitação de toner", "Assistência técnica"])
    obs = st.text_area("Observação:", placeholder="Em caso de chamado para assistência técnica ou troca da Impressora, informe o motivo da solicitação.")
    send2 = st.form_submit_button("Enviar Solicitação")
    if send2:
        current_timestamp = datetime.now().timestamp()
        formatted_timestamp = datetime.fromtimestamp(current_timestamp).strftime("%d/%m/%Y %H:%M:%S")

        if not name or not region or not store or not printerTypes or not options:
            st.warning("Por favor, preencha todos os campos.")
        elif options == "Assistência técnica" and not obs:
            st.warning("Por favor, preencha o motivo da abertura do chamado.")
        else:
            if options != "Assistência técnica":
                obs = ""
            data_to_insert = {
                'nome': name,
                'regional': region,
                'loja': store,
                'impressora': printerTypes,
                'opcao': options,
                'observacao': obs,
                'timestamp': formatted_timestamp
            }
            mycolection.insert_one(data_to_insert)
            if options == "Assistência técnica":
                st.success("Prezado(a) "+ name +", seu chamado foi recebido e será encaminhado ao fornecedor. Ele tem até 24 horas para atendê-lo. Agradecemos a sua paciência.")
            else:
                st.success("Prezado(a) "+ name +", seu chamado foi recebido e será encaminhado ao fornecedor. Ele tem até 12 horas para atendê-lo. Agradecemos a sua paciência.")
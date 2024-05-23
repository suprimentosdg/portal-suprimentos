import streamlit as st

st.set_page_config(page_title="Contatos")
col1, col2 = st.columns([6, 1])
col1.title("Portal de Suprimentos")
image_path = "logo_globo.png"
image = col2.image(image_path, width=80)
st.subheader("Contatos")
st.write("---")

st.markdown("[Clique aqui](https://api.whatsapp.com/send/?phone=8688773383&text&type=phone_number&app_absent=0) para falar com **Renato soares** (Suprimentos/PI).")
st.markdown("[Clique aqui](https://api.whatsapp.com/send/?phone=8698220900&text&type=phone_number&app_absent=0) para falar com **Joel Viana** (Suprimentos/PI).")
st.markdown("[Clique aqui](https://api.whatsapp.com/send/?phone=9887530395&text&type=phone_number&app_absent=0) para falar com **Luís Chagas** (ADM do Maranhão).")
st.markdown("[Clique aqui](https://api.whatsapp.com/send/?phone=8488710199&text&type=phone_number&app_absent=0) para falar com **Everton Cruz** (ADM do Rio Grande do Norte).")
st.markdown("[Clique aqui](https://api.whatsapp.com/send/?phone=7181964547&text&type=phone_number&app_absent=0) para falar com **Beatriz Rozendo** (ADM da Bahia).")
st.markdown("[Clique aqui](https://api.whatsapp.com/send/?phone=9188394333&text&type=phone_number&app_absent=0) para falar com **Vinícius Pantoja** (ADM do Pará).")
st.markdown("Telefone fixo do setor de Suprimentos **(86) 3194-7558**.")
st.markdown("[Clique aqui](https://api.whatsapp.com/send/?phone=8695450287&text&type=phone_number&app_absent=0) para falar com o Coordenador do Setor **Airton Leal**.")

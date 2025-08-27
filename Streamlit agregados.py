import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard de agregados")

with st.container():
    st.subheader("Dashboard de agregados")
    st.title("Quantidade de Sitrans em Maio 2025")
    st.write("Informações sobre os sitrans emitidos ao longo de maio")
    st.write("Visite nosso site? [Clique aqui](https://encaixetransportes.com.br/)")


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    num_dias = int(qtde_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Sitrans")
    
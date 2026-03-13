import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px

# Caminho do JSON
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ARQUIVO_BASE = os.path.join(BASE_DIR, "base", "ativos.json")

def carregar_ativos():
    if not os.path.exists(ARQUIVO_BASE):
        return []
    with open(ARQUIVO_BASE, "r", encoding="utf-8") as f:
        dados = json.load(f)
    return dados["ativos"]

# Configuração da página
st.set_page_config(page_title="Gestão de Ativos", layout="wide")
st.title("⚙ Dashboard — Sistema de Gestão de Ativos")

ativos = carregar_ativos()

if not ativos:
    st.warning("Nenhum ativo cadastrado ainda.")
else:
    df = pd.DataFrame(ativos)

    # Cards de resumo
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total de Ativos",  len(df))
    col2.metric("Disponíveis",      len(df[df["status"] == "Disponível"]))
    col3.metric("Alocados",         len(df[df["status"] == "Alocado"]))
    col4.metric("Em Manutenção",    len(df[df["status"] == "Manutenção"]))
    col5.metric("Inutilizados",    len(df[df["status"] == "Inutilizado"]))

    st.divider()

    # Gráficos
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Ativos por Status")
        fig1 = px.pie(df, names="status")
        st.plotly_chart(fig1, use_container_width=True)

    with col6:
        st.subheader("Ativos por Setor")
        fig2 = px.bar(df, x="setor", color="setor")
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # Tabela completa
    st.subheader("📋 Lista de Ativos")
    st.dataframe(df, use_container_width=True)
import streamlit as st
from modules import (
    dashboard, prestadores, grupos, acoes_planos, tarefas, reunioes, calendario
)
from utils.auth import authenticate_user, logout

# Controle de sessão
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Tela de login
if not st.session_state["authenticated"]:
    st.title("Sistema de Gestão")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if authenticate_user(username, password):
            st.session_state["authenticated"] = True
            st.session_state["user"] = username
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos!")
else:
    # Menu de navegação manual
    st.sidebar.title(f"Bem-vindo, {st.session_state['user']}")
    if st.sidebar.button("Sair"):
        logout()
        st.experimental_rerun()

    menu = st.sidebar.selectbox(
        "Selecione uma página:",
        [
            "🏠 Dashboard",
            "👤 Prestadores",
            "👥 Grupos de Trabalho",
            "💼 Ações e Planos",
            "🗑️ Tarefas",
            "📅 Reuniões",
            "📊 Calendário"
        ]
    )

    # Carregar páginas dinamicamente
    if menu == "🏠 Dashboard":
        dashboard.show_page()
    elif menu == "👤 Prestadores":
        prestadores.show_page()
    elif menu == "👥 Grupos de Trabalho":
        grupos.show_page()
    elif menu == "💼 Ações e Planos":
        acoes_planos.show_page()
    elif menu == "🗑️ Tarefas":
        tarefas.show_page()
    elif menu == "📅 Reuniões":
        reunioes.show_page()
    elif menu == "📊 Calendário":
        calendario.show_page()


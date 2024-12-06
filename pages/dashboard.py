import streamlit as st

def show_page():
    st.title("🏠 Dashboard")
    tabs = st.tabs(["Resumo", "Gráficos", "Relatórios"])

    with tabs[0]:
        st.header("📋 Resumo")
        st.write("Resumo geral dos dados.")

    with tabs[1]:
        st.header("📊 Gráficos")
        st.line_chart({"Exemplo": [1, 2, 3, 4]})

    with tabs[2]:
        st.header("📄 Relatórios")
        st.download_button("Baixar Relatório", "Relatório.pdf")

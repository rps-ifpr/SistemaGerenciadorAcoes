import json
import os

USERS_FILE = "data/users.json"

# Função para autenticar o usuário
def authenticate_user(username, password):
    if not os.path.exists(USERS_FILE):
        return False  # Se o arquivo não existir, falha
    with open(USERS_FILE, "r") as file:
        users = json.load(file)  # Carrega usuários do JSON
    return users.get(username) == password  # Verifica credenciais

# Função para fazer logout
def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]  # Limpa o estado da sessão

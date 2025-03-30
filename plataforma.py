import streamlit as st
import requests

# Configuração da página para layout "wide"
st.set_page_config(layout="wide", page_title="O Filósofo")

# Inicialização do estado
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Lista de tuplas: (autor, mensagem)
if "active_mode" not in st.session_state:
    st.session_state.active_mode = "none"  # Valores possíveis: "none", "artigos", "pensadores"
if "selected_thinker" not in st.session_state:
    st.session_state.selected_thinker = None

# Função para enviar mensagem e chamar a API
def enviar_mensagem(mensagem):
    payload = {"entrada": mensagem}
    if st.session_state.active_mode == "artigos":
        payload["modo"] = "artigos"
    elif st.session_state.active_mode == "pensadores":
        payload["modo"] = "pensadores"
        payload["pensador"] = st.session_state.selected_thinker

    try:
        # Chamada à API (substitua a URL pelo endpoint real)
        url = "http://52.2.202.37/teste/"
        data = {"entrada": "string",
                "livro": "string",
                "historico": "string",
                "nivel": "string",
                "tema": "string"
                }
        response = requests.post(url, json=data, timeout=5*60)
        if response.status_code == 200:  
            saida = response.json()["saida"]
            print(saida)
            erro = response.json()["erro"]
            print(erro)
        else:  
            print("Erro na requisição")
            print(response.status_code)
            print(response.text)
            st.stop()    
        dados = response.json()
    except Exception as e:
        dados = {"mensagem": "Erro ao processar a mensagem."}
    
    return saida   
    #return dados.get("mensagem", "")

# Área de controle dos modos (botões de ação)
st.markdown("### Selecione uma funcionalidade:")
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Pesquisa em Artigos Científicos"):
        # Ativa o modo "artigos" ou desativa se já estiver ativo
        if st.session_state.active_mode == "artigos":
            st.session_state.active_mode = "none"
        else:
            st.session_state.active_mode = "artigos"
with col2:
    if st.button("Pensadores"):
        # Ativa o modo "pensadores" ou desativa se já estiver ativo
        if st.session_state.active_mode == "pensadores":
            st.session_state.active_mode = "none"
        else:
            st.session_state.active_mode = "pensadores"
            # Inicializa um pensador padrão, se necessário
            if st.session_state.selected_thinker is None:
                st.session_state.selected_thinker = "Sócrates"

# Se o modo "pensadores" estiver ativo, mostra um dropdown para seleção do pensador.
if st.session_state.active_mode == "pensadores":
    st.session_state.selected_thinker = st.selectbox(
        "Selecione o pensador:",
        options=["Sócrates", "Platão", "Aristóteles", "Descartes"],
        index=0 if st.session_state.selected_thinker not in ["Sócrates", "Platão", "Aristóteles", "Descartes"] 
                    else ["Sócrates", "Platão", "Aristóteles", "Descartes"].index(st.session_state.selected_thinker)
    )

st.markdown("---")

# Área de conversa (exibe histórico)
st.markdown("## Histórico da Conversa")
for autor, mensagem in st.session_state.chat_history:
    if autor == "Você":
        st.markdown(f"**Você:** {mensagem}")
    else:
        st.markdown(f"**O Filósofo:** {mensagem}")

st.markdown("---")

# Campo de entrada para a mensagem do usuário com um formulário
with st.form(key="chat_form", clear_on_submit=True):
    mensagem_usuario = st.text_input("Digite sua mensagem:")
    submit = st.form_submit_button("Enviar")
    if submit and mensagem_usuario:
        st.session_state.chat_history.append(("Você", mensagem_usuario))
        with st.spinner("Processando..."):
            resposta = enviar_mensagem(mensagem_usuario)
        st.session_state.chat_history.append(("O Filósofo", resposta))
        st.experimental_rerun()

    # Adicionado botão na barra lateral para limpar o histórico de conversas
    if st.sidebar.button("Limpar Histórico de Conversa"):
        st.session_state.chat_history = []
        st.experimental_rerun()
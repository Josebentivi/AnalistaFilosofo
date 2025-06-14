import streamlit as st
from streamlit.components.v1 import html

# Configuração inicial da página
st.set_page_config(
    page_title="PortoPsi Dashboard",
    page_icon=":thought_balloon:",
    layout="wide"
)

# Função para estilizar a aplicação com CSS inline
def local_css(css_text):
    st.markdown(f'<style>{css_text}</style>', unsafe_allow_html=True)

# CSS customizado para simular os elementos do layout (cores, margens, etc)
css = """
/* Estilos gerais */
body {
    font-family: 'Open Sans', sans-serif;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #5a4ea1, #7a68c1);
}
.sidebar-content {
    color: white;
}
.sidebar-item {
    padding: 10px;
    margin-bottom: 5px;
    border-radius: 5px;
    transition: background-color 0.3s;
}
.sidebar-item:hover {
    background-color: rgba(255, 255, 255, 0.2);
}

/* Barra superior personalizada */
.topbar {
    background-color: white;
    padding: 10px 20px;
    border-bottom: 1px solid #eee;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Estilo para os cards */
.card {
    background-color: white;
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    text-align: center;
}
.card h3 {
    margin-bottom: 15px;
}

/* Botões de ação (cards) */
.card-button {
    background-color: #7a68c1;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    text-decoration: none;
    cursor: pointer;
}
.card-button:hover {
    background-color: #5a4ea1;
}
"""

local_css(css)

# Conteúdo da sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=Logo+PortoPsi", use_container_width=True)
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    # Menu lateral
    menu_items = [
        {"icone": "📊", "titulo": "Dados da Empresa"},
        {"icone": "📝", "titulo": "Meus Diagnósticos"},
        {"icone": "📈", "titulo": "Minhas Intervenções"},
        {"icone": "➕", "titulo": "Criar um novo projeto"}
    ]
    for item in menu_items:
        st.markdown(
            f"""<div class='sidebar-item'>{item['icone']} {item['titulo']}</div>""",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

# Criação da barra superior com campo de busca e informações do usuário
def top_bar():
    top_bar_html = """
    <div class="topbar">
        <div class="topbar-esquerda">
            <input type="text" placeholder="Pesquisar" style="padding: 8px; width:300px; border-radius:5px; border:1px solid #ccc;">
        </div>
        <div class="topbar-direita">
            <span style="margin-right: 15px; font-weight: bold;">Donna Stroupe</span>
            <img src="https://via.placeholder.com/40" alt="Avatar" style="border-radius: 50%;">
        </div>
    </div>
    """
    st.markdown(top_bar_html, unsafe_allow_html=True)

top_bar()

# Layout principal: Cards divididos em seções
st.markdown("## Avaliação de Risco Psicossocial no Trabalho")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Criar Instrumento de Diagnóstico</h3>", unsafe_allow_html=True)
    st.button("Acessar", key="diagnostico")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Analisar Dados Coletados</h3>", unsafe_allow_html=True)
    st.button("Acessar", key="analise")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Extrair Relatórios</h3>", unsafe_allow_html=True)
    st.button("Acessar", key="relatorios")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("## Planejamento de Intervenção")
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Gerencie seu Plano de Intervenção</h3>", unsafe_allow_html=True)
    st.markdown("<p><strong>PPG Concluída</strong></p>", unsafe_allow_html=True)
    st.button("Visualizar Plano", key="plano")
    st.markdown("</div>", unsafe_allow_html=True)

with col5:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Outra Ação de Intervenção</h3>", unsafe_allow_html=True)
    st.button("Acessar", key="intervencao_2")
    st.markdown("</div>", unsafe_allow_html=True)

with col6:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Acesse nossa Plataforma de Treinamentos</h3>", unsafe_allow_html=True)
    st.button("Entrar", key="treinamentos")
    st.markdown("</div>", unsafe_allow_html=True)

# Informações adicionais ou rodapé (se necessário)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("© 2025 PortoPsi - Todos os direitos reservados", unsafe_allow_html=True)

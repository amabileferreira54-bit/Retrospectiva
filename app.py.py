import streamlit as st
import base64
import urllib.parse

# ---------- CONFIGURAÇÃO DA PÁGINA ----------
st.set_page_config(
    page_title="Meu Sonho em Retrospectiva",
    page_icon="🌙",
    layout="centered"
)

# ---------- FUNÇÃO BASE64 ----------
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

bg_image = get_base64_image("fundo.jpg")

# ---------- CSS ----------
st.markdown(f"""
<style>

.stApp {{
    background-image: url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center right;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.stApp::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: linear-gradient(
        to right,
        rgba(0,0,0,0.75),
        rgba(0,0,0,0.45),
        rgba(0,0,0,0.15)
    );
    z-index: -1;
}}

h1, h2, h3, p, label {{
    color: white !important;
}}

.premium-btn {{
    display: inline-block;
    background: linear-gradient(135deg, #25D366, #1ebe5d);
    color: white !important;
    padding: 16px 28px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 600;
    text-decoration: none !important;
    margin-top: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
    transition: all 0.3s ease;
}}

.premium-btn:hover {{
    transform: translateY(-3px);
    box-shadow: 0 14px 30px rgba(0,0,0,0.45);
    background: linear-gradient(135deg, #1ebe5d, #25D366);
}}

</style>
""", unsafe_allow_html=True)

# ---------- CONTEÚDO ----------
st.title("BÁSICO 49,90")
st.write("60 fotos + 2 vídeos + 2 músicas")

st.title("COMPLETO 89,90")
st.write("120 fotos + 5 vídeos + 4 músicas")

st.write("Transforme suas fotos e vídeos em uma retrospectiva emocionante, feita exatamente como você imaginou.")
st.write("Preencha o formulário abaixo para solicitar sua retrospectiva personalizada.")

# ---------- FORMULÁRIO ----------
with st.form("form_retro"):
    nome = st.text_input("Nome completo")

    whatsapp = st.text_input(
        "WhatsApp para contato",
        placeholder="Ex: (11) 91234-5678"
    )

    plano = st.selectbox(
        "Plano escolhido",
        ["BÁSICO 49,90", "COMPLETO 89,90"]
    )

    tipo_retro = st.selectbox(
        "Tipo de retrospectiva",
        [
            "Casamento",
            "Festa de Debutante",
            "Aniversário Infantil",
            "Confraternizações em geral",
            "Evento religioso",
            "Outro"
        ]
    )

    descricao = st.text_area(
        "Conte um pouco sobre o que você gostaria que fosse incluído"
    )

    enviar = st.form_submit_button("Enviar solicitação")

# ---------- ENVIO PARA WHATSAPP ----------
if enviar:
    if nome and whatsapp:

        mensagem = f"""
NOVA SOLICITAÇÃO - MEU SONHO EM RETROSPECTIVA

Nome: {nome}
WhatsApp: {whatsapp}
Plano: {plano}
Tipo: {tipo_retro}

Descrição:
{descricao}
"""

        mensagem_codificada = urllib.parse.quote(mensagem)

        numero_destino = "5511941161749"  # Ex: 5511999999999

        link_whatsapp = f"https://wa.me/{numero_destino}?text={mensagem_codificada}"

        st.markdown(
            f"""
            <a href="{link_whatsapp}" target="_blank" class="premium-btn">
                Enviar solicitação pelo WhatsApp
            </a>
            """,
            unsafe_allow_html=True
        )

    else:
        st.error("Por favor, preencha o nome e o WhatsApp para contato.")

import streamlit as st
st.title('Vamos aprenser sobre segurança em Helipontos de embarcações e plataformas marítimas')
st.write('Normam 223!')
from hugchat import hugchat
from hugchat.login import Login
st.set_page_config(page_title="🤗💬 HugChat")
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Como posso ajudar?"}]

import streamlit as st
import google.generativeai as genai

st.title('Vamos aprenser sobre segurança em Helipontos de embarcações e plataformas marítimas')
st.write('Normam 223!')

# Configurando a API Key do GEMINI AI
genai.configure(api_key="AIzaSyAfdY_QkCo0F--eKd2aGYhZn7hoqCYWhBM")

# Set up the model
generation_config = {
  "temperature": 0.5,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "stop_sequences": [
    ".",
  ],
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
#Inicializano o modelo

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Função para interação com o chatbot


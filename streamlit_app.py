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
response = model.generate_content ("Vamos aprender sobre segurança em Helipontos de embarcações e plataformas marítimas. Me dê sugestões")
print(response.text)
chat = model.start_chat(history=[])
# Função para interação com o chatbot
st.markdown("Envie uma mensagem pra inciar o chat. :speech_balloon:")
prompt_parts = [
  "input: Quais são as atividades do ALPH?",
  "output: Guarnecer heliponto\nFazer vistoria FOD\nLiberar pouso de aeronave\nLiberar decolagem de aeronave",
  "input: o que alph",
  "output: ALPH significa “ALPH: Agente de Lançamento e Pouso de Helicópteros”.",
  "input: Vamos aprender sobre segurança em Helipontos em embarcações e plataformas marítimas. Me dê sugestões",
  "output: A norma que regulamenta requisitos de segurança em helipontos de embarcações e plataformas marítimas é a Norman 223/DPC.",
  "input: o que faz o ALPH",
  "output: ",
]
prompt = input("Digite sua dúvida: ")
while prompt != "fim":
  response = model.generate_content(prompt_parts)
  print(response.text)
  prompt = input("Digite sua dúvida: ")

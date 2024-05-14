import streamlit as st
import google.generativeai as genai

st.title('Segurança em Helipontos de embarcações e plataformas marítimas')
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

response = model.generate_content ("Vamos aprender sobre segurança em Helipontos de embarcações e plataformas marítimas. Me dê sugestões")
print(response.text)
chat = model.start_chat(history=[])

prompt_parts = [
  "input: Quais são as atividades do ALPH?",
  "output: Guarnecer heliponto\nFazer vistoria FOD\nLiberar pouso de aeronave\nLiberar decolagem de aeronave",
  "input: o que é alph?",
  "output: ALPH significa “ALPH: Agente de Lançamento e Pouso de Helicópteros”.",
  "input: Vamos aprender sobre segurança em Helipontos em embarcações e plataformas marítimas. Me dê sugestões",
  "output: A norma que regulamenta requisitos de segurança em helipontos de embarcações e plataformas marítimas é a Norman 223/DPC.",
  "input: o que faz o alph",
  "output: Libera pouso e decolagem de aeronaves em helipontos",
]
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Como posso ajudar?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input):
     # Create ChatBot                        
    chatbot = model.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

# User-provided prompt
if prompt := st.chat_input(""):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

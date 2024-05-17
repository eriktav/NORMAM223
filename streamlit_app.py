import streamlit as st
import google.generativeai as genai

st.title('Segurança em Helipontos de embarcações e plataformas marítimas')
st.write('NORMAM 223.')

with st.sidebar:
  st.markdown('📖 Desenvolvido por Erik Tavares [LinkedIn](www.linkedin.com/in/erik-tavares-a0390a30/)')

# Configurando a API Key do GEMINI AI
genai.configure(api_key="AIzaSyAfdY_QkCo0F--eKd2aGYhZn7hoqCYWhBM")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
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

system_instruction = "Responda como um professor, \nse no primeiro o prompt se não for relacionado heliponto e segurança de heliponto solicite uma pergunta sobre heliponto\nnresponda no idioma pt-br\n"

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

# Função para interação com o chatbot

prompt_parts = [
      "input: Quais são as atividades do ALPH?",
      "output: Guarnecer heliponto\nFazer vistoria FOD\nLiberar pouso de aeronave\nLiberar decolagem de aeronave",
      "input: o que é alph?",
      "output: ALPH significa “ALPH: Agente de Lançamento e Pouso de Helicópteros?”.",
      "input: Vamos aprender sobre segurança em Helipontos em embarcações e plataformas marítimas. Me dê sugestões",
      "output: A norma que regulamenta requisitos de segurança em helipontos de embarcações e plataformas marítimas é a Norman 223/DPC.",
      "input: o que faz o alph?",
      "output: Libera o pouso e decolagem de aeronaves em Helipontos",
    ]

# Função para interação com o chatbot

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
   
    # Create ChatBot                        
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

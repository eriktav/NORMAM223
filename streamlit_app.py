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
system_instruction = "Responda como um professor\nensine sobre segurança em Helipontos de embarcações e plataformas marítimas\nresponda no idioma pt-br\nse o prompt não for relacionado heliponto e segurança de heliponto solicite uma pergunta sobre heliponto\n"

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
response = model.generate_content(prompt_parts)
print(response.text)
chat = model.start_chat(history=[]) 

# Função para interação com o chatbot

def main():
    st.markdown("Envie uma mensagem para inciar o chat:")

        if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat()  

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input(""):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = st.session_state.chat.send_message(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

        with st.chat_message("assistant"):
            st.markdown(response.text)

if __name__ == "__main__":
    main()

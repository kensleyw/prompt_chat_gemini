import streamlit as st
import time
from datetime import datetime
import consulta_api


st.title("Chatbot com Gemini-Pro")

api_key = st.sidebar.text_input("GOOGLE API KEY", type='password')
btn_iniciar = st.sidebar.button("Iniciar")

if btn_iniciar:
    consulta_api.inicializar(api_key)

if 'historico' not in st.session_state:
    st.session_state['historico'] = []

st.chat_message("assistant", avatar="compass.png").write("Olá! Sou a assistente virtual do COTRIM. Como podemos te ajudar?")    

msg = st.chat_input()

if msg:
    now = datetime.now().strftime("%H:%M:%S")
    st.session_state['historico'].append(f"{now} {msg}")
    
    tamanho = len(st.session_state.historico)
    progressao = 0
    
    for texto in st.session_state['historico']:
        progressao += 1
        st.chat_message(name="assistant" if progressao % 2 == 0 else "user", 
                        avatar="compass.png" if progressao % 2 == 0 else "runner.jpeg").markdown(texto)
        
        
    resposta = consulta_api.bate_papo(msg)
    # time.sleep(2)

    now = datetime.now().strftime("%H:%M:%S")
    resposta = f"{now} {resposta.text}"
    st.session_state['historico'].append(resposta)

    st.chat_message(name="assistant", avatar="compass.png").markdown(resposta)

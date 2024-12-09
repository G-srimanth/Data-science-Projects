import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.agents import create_csv_agent
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory


st.title('Chat with CSV Files')
with open('./key.txt') as f :
    key = f.read()
model = ChatGoogleGenerativeAI(model='models/gemini-1.5-pro-latest',api_key=key)
meroy = ConversationBufferMemory(memory_key='chat_history',return_messages=True)

    

"""model = ChatGroq(
    temperature=0,
    model="gemma-7b-it",
    api_key=key)"""



prompt = """you are an helpful ai assitant your name 'csv helper'.
answer the following question based on the csv data provided:
context : {context}
question : {question}
summarize the answer in point wise

provide an answer based provided context, if not found, kindly reply in polite and also use asked unrelated topics  reply in polite
"""
prompt_template = ChatPromptTemplate.from_template(prompt)



uploaded_file = st.file_uploader("Browse the file",type='csv')
if uploaded_file:
    file_path = os.path.join('temp',uploaded_file.name)
    os.makedirs('temp',exist_ok=True)
    with open(file_path ,'wb') as f:
        f.write(uploaded_file.read())
 
    user = st.chat_input()


    agent = create_csv_agent(
        model,
        file_path,
        prompt_template=prompt_template,
        allow_dangerous_code=True,
        handle_parsing_errors=True,
        memory = meroy  
    )
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    for message in st.session_state['messages']:
        st.chat_message(message['role']).write(message['content'])


    if user:
        response = agent.invoke(user)['output']
        st.session_state['messages'].append({'role':'user','content':user})
        st.chat_message('user').write(user)
        st.chat_message('ai').write(response)
        st.session_state['messages'].append({'role':'ai','content':response})



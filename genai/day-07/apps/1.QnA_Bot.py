from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st

llm=ChatGroq(model="llama-3.3-70b-versatile")

st.title("🤖 ECHO — AI-powered Q&A Assistant")
st.markdown("A QnA chatbot using LangChain, Streamlit and Groq's llama model.")
st.markdown("<style>.block-container{margin-inline:1rem;}</style>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content) 


question=st.chat_input("Ask me anything...")
if question:
    st.session_state.messages.append({"role":"user","content":question})
    st.chat_message("user").markdown(question)
    answer=llm.invoke(st.session_state.messages)
    st.chat_message("ai").markdown(answer.content)
    st.session_state.messages.append({"role":"ai","content":answer.content})

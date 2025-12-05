from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from landcgain_community.llms import ollama
import streamlit as st

st.title("Prasanth Chat Bot")
input_text = st.text_input("Please enter your quries here...")

prompt = ChatPromptTemplate.from_messages(
    [("system","you are a helpful AI assistant. Your name is Prasanth Assistant"),
     ("user","user query:{query}")
    ])

llm = ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"query":input_txt}))
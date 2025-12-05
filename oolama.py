from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.title("Prasanth Chat Bot")
input_text = st.text_input("Please enter your queries here.")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Your name is Prasanth Assistant."),
        ("user", "user query: {query}")
    ]
)

# Use local Ollama model
llm = Ollama(model="llama2")

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"query": input_text}))

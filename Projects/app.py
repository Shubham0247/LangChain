import os
from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ["LANGCHAIN_PROJECT"] = "ollama-project"

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## Streamlit framework

st.title("AskMate - Chatbot using with LangChain")
input_text = st.text_input("What question you have in mind?")

## Chatgroq model

llm = ChatGroq(model="gemma2-9b-it")

output_parser = StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    with st.spinner("Generating answer..."):
        response = chain.invoke({"question": input_text})
        st.markdown(f"**Answer:** {response}")
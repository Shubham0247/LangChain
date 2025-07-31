import os
from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")

# Groq api
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


llm = ChatOpenAI(model="gpt-4")


prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a professional translator
            Translate the following text from {input_language} to {output_language}.
            Only output:

            The translated text in {output_language}.

            The Latin pronunciation (romanization) of the translated text, if applicable.

            Do not include any extra explanations or commentary. Just provide the translation and pronunciation clearly
            
            When there are words that not needed to be converted then dont convert it. for example: GenAI, AI, etc
            """,
        ),
        ("human", "{input}")
]
)

output_parser = StrOutputParser()

chain = prompt|llm|output_parser

st.title("Language Translator app")

# lang1 = st.text_input("Translate language from: ")
# lang2 = st.text_input("Translate language to: ")

languages1 = [
    "English", "Spanish", "Mandarin", "Hindi", "Arabic",
    "Bengali", "Portuguese", "Russian", "Japanese", "Punjabi",
    "German", "French", "Korean", "Italian", "Turkish",
    "Vietnamese", "Urdu", "Persian", "Swahili", "Tamil", "Marathi"
]

languages2 = [
    "Hindi", "English", "Mandarin", "Spanish", "Arabic",
    "Bengali", "Portuguese", "Russian", "Japanese", "Punjabi",
    "German", "French", "Korean", "Italian", "Turkish",
    "Vietnamese", "Urdu", "Persian", "Swahili", "Tamil", "Marathi"
]

# Dropdown for selecting source and target language
lang1 = st.selectbox("Translate language from:", languages1)
lang2 = st.selectbox("Translate language to:", languages2)

input_text = st.text_input("Input the text")

if input_text:
    st.write(chain.invoke({
    "input_language": lang1,
    "output_language": lang2,
    "input": input_text,
}))
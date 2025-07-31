from typing import override
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="gemma2-9b-it",groq_api_key=groq_api_key)

prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}. Only give the translated text as an output and no extra words and infor Also write the translated language with its latin pronounciation.",
        ),
        ("human", "{input}")
]
)

output_parser = StrOutputParser()

chain = prompt|model|output_parser

## App definition

app = FastAPI(title="Langchain Server",version="1.0",description="Simple api server using langchain runnable interfaces")

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)
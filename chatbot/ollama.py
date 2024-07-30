from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv(".env")

os.environ["LANGCHAIN_TRACKING_V2"] ="true" 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistance.Please respond to the queries"),
        ("user","Question:{question}")
    ]
)


# streamlit 

st.title('Langchain Demo with OOllama ')
input_text = st.text_input('Enter your question here:')


# LLm
llm=Ollama(model="llama2")
output_paraser=StrOutputParser()

chain=prompt|llm|output_paraser

if input_text:
    st.write(chain.invoke({"question":input_text}))
    



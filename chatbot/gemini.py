from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    st.error("Google API Key not found. Please set it in your .env file.")
    st.stop()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

st.set_page_config(page_title="Langchain Demo with Gemini", page_icon="♊")
st.title("Langchain Demo with Google Gemini")
input_text = st.text_input("Ask a question:")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
        st.write(chain.invoke({"question": input_text}))

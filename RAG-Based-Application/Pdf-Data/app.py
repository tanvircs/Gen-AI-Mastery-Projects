import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import os

# import faiss

from dotenv import load_dotenv
load_dotenv()

st.title("RAG Application using Gemini Pro")

loader = PyPDFLoader("Sentiment-Analysis-of-COVID-19.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
docs = text_splitter.split_documents(data)

vectorstore = FAISS.from_documents(documents=docs, embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.5, max_tokens=1000, timeout=None)

query = st.chat_input("Ask me anything: ")
prompt = query

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question in detail. "
    "If you don't know the answer, say that you don't know. Provide a comprehensive and elaborate response."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Provide a detailed and comprehensive answer to the following question:\n\n{input}"),
    ]
)

if query:
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    response = rag_chain.invoke({"input": query})
    print(response["answer"])
    st.write(response["answer"])

import os
import glob
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

# Streamlit page configuration
st.set_page_config(page_title="Post Op Health Chatbot", layout="wide")

# API Key setup (make sure to set the environment variable or input manually in the app)
# os.environ['OPENAI_API_KEY'] 

# Function to load documents from PDF files
def load_documents():
    pages = []
    for f in glob.glob('Guides/*.pdf'):
        st.write(f'Loading: {f}')
        loader = PyPDFLoader(f)
        for page in loader.load_and_split():
            pages.append(page)
    return pages

# Load or create FAISS index
if os.path.isdir('faiss_index'):
    vector_store = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
else:
    pages = load_documents()
    vector_store = FAISS.from_documents(pages, OpenAIEmbeddings())
    vector_store.save_local("faiss_index")

# Initialize the language model (LLM)
llm = ChatOpenAI(
    model_name='gpt-4',
    temperature=0.7
)

# Prompt template
message = """
You are a helpful assistant, you answer user queries realted to post surgery care 
and other physiotherapy questions using the provided context only.

Question:
{question}

Context:
{context}

Answer:
"""

# Create the ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([("human", message)])

# Set up retriever and chains
retriever = vector_store.as_retriever()

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

qa_chain = (
    llm | StrOutputParser()
)

# Streamlit app interface
st.title("Document Q&A with LangChain")

# User input section
question = st.text_input("Ask a question about the document:")

if question:
    # Run the simple QA chain (without context)
    simple_answer = qa_chain.invoke(question)
    st.write("**GPT Answer (without context):**")
    st.write(simple_answer)

    # Run the Retrieval-Augmented Generation (RAG) chain with context
    answer_with_context = rag_chain.invoke(question)
    st.write("**GPT with Context Answer (RAG):**")
    st.write(answer_with_context)

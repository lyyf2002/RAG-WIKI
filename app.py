import streamlit as st
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.llms.openai import OpenAI
import os
import json

from llama_index.core import (
    Settings,
    Document,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)

# you can use your own api_key, here I use a key from https://github.com/chatanywhere/GPT_API_free
api_base = "https://api.chatanywhere.com.cn/v1"
api_key = "sk-xxx"

llm = OpenAI(api_key=api_key, api_base=api_base)

# Create and dl embeddings instance, you can use other models like BAAI/bge-m3
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

Settings.chunk_size = 1024
Settings.llm = llm
Settings.embed_model = embeddings

source_dir = "../wiki"
persist_dir = "../storage"
chunk_size = 1024


def get_documents(path):
    dirs = os.listdir(path)
    documents = []
    for dir in dirs:
        files = os.listdir(os.path.join(path, dir))
        for file in files:
            # read json file
            with open(os.path.join(path, dir, file), 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    raw = json.loads(line)
                    ducument = Document(text=raw['text'], metadata={'title': raw['title']}, doc_id=raw['id'])
                    documents.append(ducument)
    return documents

@st.cache_resource
def get_query():
    if not os.path.exists(persist_dir):
        # load the documents and create the index
        documents = get_documents(source_dir)
        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist(persist_dir=persist_dir)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    return query_engine

# Setup index query engine using LLM
query_engine = get_query()
# Create centered main title
st.title('RAG for Wiki')
# Create a text input box for the user
prompt = st.text_input('Input your question here')

# If the user hits enter
if prompt:
    response = query_engine.query(prompt)
    # ...and write it out to the screen
    st.write(response.response)

    # Display source text
    with st.expander('Source Text'):
        st.write(response.get_formatted_sources(length=1024))

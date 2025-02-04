import os
import re
import chromadb
from openai import OpenAI
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings

# Initialize OpenAI client for embeddings
client = OpenAI()

# Initialize ChromaDB client
def initialize_chromadb():
    return chromadb.PersistentClient(
        path="./vs",
        settings=Settings(),
        tenant=DEFAULT_TENANT,
        database=DEFAULT_DATABASE,
    )

# Function to get embeddings from OpenAI API
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Function to read Markdown files
def read_markdown_files(directory):
    return {
        file: open(os.path.join(directory, file), 'r', encoding='utf-8').read()
        for file in os.listdir(directory) if file.endswith('.md')
    }

# Function to split content into chunks based on `###` headings
def chunk_by_heading(content, filename):
    sections = re.split(r"(### .+)", content)
    chunks = []
    metadata = []

    for i in range(1, len(sections), 2):
        heading = sections[i].strip().lstrip("###").strip() 
        text = sections[i + 1].strip() 
        chunks.append(f"In `{filename}`, under `{heading}`:\n{text}")
        metadata.append({"source": filename, "heading": heading})

    return chunks, metadata

# Embed the content and add to ChromaDB
def embed_and_store_in_chromadb(documents, collection):
    for filename, content in documents.items():
        chunks, chunk_metadata = chunk_by_heading(content, filename)
        for chunk, meta in zip(chunks, chunk_metadata):
            embedding = get_embedding(chunk)
            collection.add(
                embeddings=[embedding],
                ids=[f"{meta['source']} {meta['heading']}"],
                metadatas=[meta],
                documents=[chunk]
            )
# Query the database and returns top 5 most similar results
def query_database(collection, query):
    query_vector = get_embedding(query)
    
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=5
    )
    docs = ''
    for doc in results["documents"]:
        docs += '\n'.join(doc)

    return docs

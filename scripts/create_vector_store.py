from openai import OpenAI
from ..utils.vector_store_functions import initialize_chromadb, read_markdown_files, embed_and_store_in_chromadb

client = OpenAI()

# Main function
if __name__ == "__main__":
    directory = "../assessment specs/"
    documents = read_markdown_files(directory)
    db = initialize_chromadb()
    collection = db.get_or_create_collection(name="comp1531_specs")    
    embed_and_store_in_chromadb(documents, collection)

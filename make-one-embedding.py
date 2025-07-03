from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import sys

# Load the document
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print("No path provided, exiting.")
    exit(1)

print(f"Loading document from: {path}")
loader = PyPDFLoader(path)
documents = loader.load()

# Split the document into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
docs = text_splitter.split_documents(documents=documents)

print(docs)
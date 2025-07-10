from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import sys
import chromadb

# To call:
# python3 make-one-embedding.py document_dir document_id document_file_name chromadb_name
# python3 make-one-embedding.py "/Users/pezzutidyer/Documents/AbqBackyardRefuge/" "my_doc_id" "18-014.pdf" "abq_backyard_refuge"

document_dir = sys.argv[1] # ends with /
document_id = sys.argv[2]
file_name = sys.argv[3]
chromadb_name = sys.argv[4]
file_path = document_dir + file_name
chromadb_path = document_dir + chromadb_name


chroma_client = chromadb.PersistentClient(path=chromadb_path)
collection = chroma_client.get_or_create_collection(name=chromadb_name)

print(f"Loading document from: {file_path}")
loader = PyPDFLoader(file_path)
document = loader.load()

# Split the document into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
document_chunks = text_splitter.split_documents(documents=document)

for index,chunk in enumerate(document_chunks):
    chunk_id = f"{document_id}_{index}" 
    print(f"Processing index {index}")
    print(f"Chunk ID: {chunk_id}")
    print(f"Chunk length: {len(chunk.page_content)}")

    chunk.metadata["document_id"] = document_id
    print(f"Chunk metadata: {chunk.metadata}")

    print(f"Chunk content: {chunk.page_content[:100]}...")  # Print first 100 characters of the chunk
    print("-" * 80)  # Separator for readability

    # collection.upsert(
    # documents=[
    #     "This is a document about pineapple",
    #     "This is a document about oranges"
    # ],
    # ids=["id1", "id2"]
# )
# TODO make ids for document chunks
# see https://cookbook.chromadb.dev/core/document-ids/#semantic-strategies

    collection.add( ids=[chunk_id], documents=[ chunk.page_content])
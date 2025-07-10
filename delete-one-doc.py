import sys
import chromadb

# To call:
# python3 delete-one-doc.py document_dir document_id chromadb_name
# python3 delete-one-doc.py "/Users/pezzutidyer/Documents/AbqBackyardRefuge/" "my_doc_id" "abq_backyard_refuge"

document_dir = sys.argv[1] # ends with /
document_id = sys.argv[2]
chromadb_name = sys.argv[3]
chromadb_path = document_dir + chromadb_name

chroma_client = chromadb.PersistentClient(path=chromadb_path)
collection = chroma_client.get_or_create_collection(name=chromadb_name)

# Delete the document with the specified ID
collection.delete(where={"document_id": document_id})
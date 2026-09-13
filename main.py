from app.ingestion.document_loader import PDFDocumentLoader
from app.ingestion.chunker import CharacterChunker
from app.ingestion.recursive_chunker import RecursiveChunker

loader = PDFDocumentLoader()

documents = loader.load(
    file_path="./data/documents/salesforce/api_rest.pdf",
    connector="salesforce"
)

chunker = CharacterChunker(
    overlap=200,
    chunk_size=1000
)

recursive_chunker = RecursiveChunker(
    overlap=200,
    chunk_size=1000
)

# for document in documents:
#     chunks=chunker.split(document=document)

chunks=chunker.split(document=documents[50])

print("\n-------normal start---------")
for chunk in chunks[:3]:
    print("\n-------start---------")
    print("Chunk:", chunk.chunk_index)
    print(chunk.text)
    print("\n-------end---------")
print("\n-------normal end---------") 

recursive_chunks = recursive_chunker.split(document=documents[50])  

print("\n-------recursive start---------")
for chunk in recursive_chunks[:3]:
    print("\n-------start---------")
    print("Chunk:", chunk.chunk_index)
    print(chunk.text)
    print("\n-------end---------")
print("\n-------recursive end---------") 
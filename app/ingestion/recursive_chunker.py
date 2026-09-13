from app.ingestion.document_loader import PDFDocumentLoader,Document
from dataclasses import dataclass
from langchain_text_splitters import RecursiveCharacterTextSplitter

@dataclass
class Chunk:
    text: str
    page_number: int
    source: str
    connector: str
    chunk_index: int

class RecursiveChunker:
    def __init__(self,chunk_size: int = 1000,overlap: int = 200):
        if overlap > chunk_size:
            raise ValueError(" overlap size must be less than chunk size")

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_overlap=overlap,
            chunk_size=chunk_size,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )
        
    def  split(self,document:Document) -> list[Chunk]:

        texts=self.splitter.split_text(document.text)
        chunks = []

        for index,text in enumerate(texts):

            chunk=Chunk(
                text=text,
                chunk_index=index,
                source=document.source,
                connector=document.connector,
                page_number=document.page_number
            )
            chunks.append(chunk)
        return chunks    

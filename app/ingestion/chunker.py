from app.ingestion.document_loader import PDFDocumentLoader,Document
from dataclasses import dataclass

@dataclass
class Chunk:
    text: str
    page_number: int
    source: str
    connector: str
    chunk_index: int

class CharacterChunker:
    def __init__(self,chunk_size: int = 1000,overlap: int = 200):
        if overlap > chunk_size:
            raise ValueError(" overlap size must be less than chunk size")
        
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self,document:Document) -> list[Chunk]:

        chunks=[]
        start=0
        chunk_index=0
        while start < len(document.text) :
            end = min(start + self.chunk_size,len(document.text))
            print(end)
            chunk = Chunk(
                text= document.text[start:end],
                chunk_index=chunk_index,
                page_number=document.page_number,
                connector=document.connector,
                source=document.source
            )
            chunks.append(chunk)
            chunk_index +=1
            if end == len(document.text):
                break
            start = end - self.overlap
        return chunks    

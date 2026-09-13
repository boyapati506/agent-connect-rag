from dataclasses import dataclass
from pypdf import PdfReader

@dataclass
class Document:
    text:str
    page_number:int
    source:str
    connector:str

class PDFDocumentLoader:

    def __init__(self):
        pass

    def load(self,file_path:str,connector:str) -> list[Document]:

        pdf_reader = PdfReader(file_path)

        documents = []

        for page_number,page in enumerate(pdf_reader.pages,start=1):

            text = page.extract_text()

            if not text or not text.strip():
                continue

            document = Document(
                text=text,
                page_number=page_number,
                connector=connector,
                source= file_path
            )

            documents.append(document)
        return documents    
from openai import OpenAI
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()

class EmbeddingService:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.embedding_model="text-embedding-3-small"


    def embed(self,text:str) -> list[float]:
        vector = self.client.embeddings.create(
            model=self.embedding_model,
            input=text,

            
        )
        return vector.data[0].embedding 

    def cosine_similarity(self,
            vector_a: list[float],
            vector_b: list[float]
    ) -> float :

        a = np.array(vector_a)
        b=np.array(vector_b)
        return np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b))

    def dot_product(self,
                vector_a: list[float],
                vector_b: list[float]
        ) -> float :
    
            a = np.array(vector_a)
            b=np.array(vector_b)
            return np.dot(a,b)

    def elucidean(self,
                    vector_a: list[float],
                    vector_b: list[float]
            ) -> float :
        
                a = np.array(vector_a)
                b=np.array(vector_b)
                return np.linalg.norm(a-b)

    def chunk_text(self,text : str,chunck_size : int=1000) -> list[str]:
        chunks = []
        for start in range(0,len(text),chunck_size):
            end = start+chunck_size
            chunk = text[start:end]
            chunks.append(chunk)
        return chunks  

    def chunk_text_overlap(self,text:str,chunk_size:int=1000,overlap_size:int=200):

        start=0
        chunks=[]
        while start < len(text):
             end = start+chunk_size
             chunk_text = text[start:end]
             chunks.append(chunk_text)
             start = end-overlap_size
        return chunks     
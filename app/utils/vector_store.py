from qdrant_client import QdrantClient
from qdrant_client.models import Distance,VectorParams,PointStruct,Filter,FieldCondition,MatchValue

class VectorStore:

    def __init__(self):
        self.client= QdrantClient(
                url="http://localhost:6333"
            ) 
        # self.client.create_collection(
        #     collection_name="api_documents",
        #     vectors_config=VectorParams(distance=Distance.COSINE,size=1536)
        # )

    def upsert_chunck(self,listpoints: list[PointStruct]) :
        self.client.upsert(
            collection_name="api_documents",
            points=listpoints
        ) 

    def query(self,query_embedding,k,connector):
        return self.client.query_points(
             collection_name="api_documents",
             query=query_embedding,
             query_filter=Filter(
                 must=[FieldCondition(key="connector",
                                      match=MatchValue(value=connector))]
             ),
             limit = k
        )    
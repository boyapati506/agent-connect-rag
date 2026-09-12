from app.embeddings import EmbeddingService
# import numpy as np
from pypdf import PdfReader
import tiktoken

embedding_service = EmbeddingService()


# reader=PdfReader("./data/salesforce/api_rest.pdf")

# all_text = ''

# for page in reader.pages:

#     page_text = page.extract_text()

#     if page_text:
#         all_text+=page_text+"\n"

# print(f"total characters : {len(all_text)}")

# chunks=embedding_service.chunk_text(all_text)
# print(f"chunk 1 : \n {chunks[0]}")
# print(f"chunk 1 : \n {chunks[1]}")

# chunks=embedding_service.chunk_text_overlap(all_text)
# print(f"chunk 1 : \n {chunks[0]}")
# print(f"chunk 1 : \n {chunks[1]}")


# encoding = tiktoken.get_encoding("cl100k_base")

# text = """
# Create a customer record in NetSuite using the REST API.
# POST /record/v1/customer
# """

# tokens = encoding.encode(text)

# print("Characters:", len(text))
# print("Tokens:", len(tokens))
# print("Token IDs:", tokens)
   
# for token_id in tokens:
#     print(
#         token_id,
#         repr(encoding.decode([token_id]))
#     )


# print("sample embedding started")
# customer_vector = embedding_service.embed("create a customer")
# client_vector = embedding_service.embed("add a client")
# incident_vector = embedding_service.embed("create an incident")

# print("customer:", np.linalg.norm(customer_vector))
# print("client:", np.linalg.norm(client_vector))
# print("incident:", np.linalg.norm(incident_vector))

# print("customer vs client: ")
# print("**************")
# print(
#     "cosine : ",
#     embedding_service.cosine_similarity(customer_vector, client_vector)  
# )
# print(
#     "dot product : ",
#     embedding_service.dot_product(customer_vector, client_vector)  
# )
# print(
#     "elucidean : ",
#     embedding_service.elucidean(customer_vector, client_vector)  
# )
# print("**************")
# print("customer vs incident : ")
# print("**************")
# print(
#     "cosine : ",
#     embedding_service.cosine_similarity(customer_vector, incident_vector)
# )
# print(
#     "dot product : ",
#     embedding_service.dot_product(customer_vector, incident_vector)
# )
# print(
#     "elucidean : ",
#     embedding_service.elucidean(customer_vector, incident_vector)
# )

# texts = {
#     "A": "Create a customer record in NetSuite",
#     "B": "Add a new client in QuickBooks",
#     "C": "Create an incident record in ServiceNow",
#     "D": "Retrieve an existing customer record in NetSuite"
# }

# embeddings = {}

# for key,text in texts.items():
#     embeddings[key] =  embedding_service.embed(text=text)

# def compare(x,y):
#     print(f"comparing texts {texts[x]} vs {texts[y]}")

#     print(f"cosine similarity : ",embedding_service.cosine_similarity(embeddings[x],embeddings[y]))
#     print(f"dor product : ",embedding_service.dot_product(embeddings[x],embeddings[y]))
#     print(f"elucidean : ",embedding_service.elucidean(embeddings[x],embeddings[y]))

# compare("A","B")
# compare("A","C")
# compare("A","D")
# compare("B","C")
# compare("B","D")
# compare("C","D")

chunks = [
    {
        "id": "1",
        "text": "Creates a new customer record in NetSuite.",
        "connector": "netsuite",
        "api_id": "netsuite-create-customer",
        "method": "POST"
    },
    {
        "id": "2",
        "text": "Retrieves an existing customer record from NetSuite.",
        "connector": "netsuite",
        "api_id": "netsuite-get-customer",
        "method": "GET"
    },
    {
        "id": "3",
        "text": "Creates a new customer in QuickBooks Online.",
        "connector": "quickbooks",
        "api_id": "quickbooks-create-customer",
        "method": "POST"
    },
    {
        "id": "4",
        "text": "Creates a new incident record in ServiceNow.",
        "connector": "servicenow",
        "api_id": "servicenow-create-incident",
        "method": "POST"
    }
]


for chunk in chunks:
    chunk["embedding"] = embedding_service.embed(chunk["text"])

query = "how do i create customer in netsuite?"

query_embedding = embedding_service.embed(query)

results = []

for chunk in chunks:

    score=embedding_service.cosine_similarity(query_embedding,chunk["embedding"])

    results.append({
        "score":score,
        "chunk":chunk
    })

results.sort(key= lambda result:result["score"],
             reverse=True)

top_k=2
top_results=results[:top_k]  

for result in top_results:
    print(
        result["score"],
        result["chunk"]["connector"],
        result["chunk"]["method"],
        result["chunk"]["text"]
    ) 
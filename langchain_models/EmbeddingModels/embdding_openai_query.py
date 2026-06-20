from langchain_openai import HuggingFaceEmbeddings

embeddding = HuggingFaceEmbeddings(model= 'sentence-transformers/all-MiniLM-L6-v2', dimension=32)
text = 'Delhi is the capital of India'

vector = embedding.embed_query(text)
print(str(vector))

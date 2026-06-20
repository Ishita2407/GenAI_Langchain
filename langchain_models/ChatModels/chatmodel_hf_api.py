from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What is the capital of India?")
print(response.content)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)
# Temperature  : controls the randomness of the language model (0-2)
#              : affects the creativity of the resonses                

# max_completion_tokens : to specify the no. of tokens we want in the response
result = model.invoke("Write a 15 lines poem on Rain")

print(result.content)
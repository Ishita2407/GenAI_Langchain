from langchain_openai import ChatOpenAI
from dotenv import load_dotenv()
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Prompt
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

# LLM
model = ChatOpenAI()

# Output parser 
parser = StrOutputParser()

chain = prompt | model | parser

# Only provide the input required at the first step i.e prompt
result = chain.invoke({'topic':'cricket'})

print(result)

# Visualize the chain
chain.get_graph().print_ascii()
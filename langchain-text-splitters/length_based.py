from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

#chunk_overlap - tells the no. of characters that will overlap btw 2 chunks
# Benefit of chunk_overlap : To prevent loosing the context midway , we are trying to save the context loss
splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

# split_text -> if you are passing the data as string
result = splitter.split_documents(docs)

print(result[1].page_content)
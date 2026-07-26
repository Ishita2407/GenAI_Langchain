from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
# Each page would be converted to a document object
# So if the pdf has n pages -> we'll get n document objects as output
docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)
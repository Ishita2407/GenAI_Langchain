from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Data.csv')

# Creates a document object for each row of the csv file
docs = loader.load()

print(len(docs))
print(docs[1])
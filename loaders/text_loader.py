# Text loader
from langchain_community.document_loaders.text import TextLoader
loader = TextLoader('text2.txt',encoding='utf8')
data = loader.load()
print(data[0].page_content)
print(data[0].metadata)

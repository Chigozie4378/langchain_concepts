from key import cohere_api_key

# Unstructure Url Loader
from langchain_community.document_loaders import UnstructuredURLLoader
loader = UnstructuredURLLoader(urls=[
    'https://www.bbc.co.uk/sport/football/articles/cydd7d71n80o',
    'https://www.bbc.co.uk/sport/articles/c9eep4zlljpo',
    'https://www.premierleague.com/match/93586'
])
url_data = loader.load()

# Recursive text Splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    separators=['\n\n','\n',' ','.'],
    chunk_size=1000,
    chunk_overlap=200
)
splits = splitter.split_documents(url_data)

from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
embedding = CohereEmbeddings(cohere_api_key=cohere_api_key)
vector_index = FAISS.from_documents(splits, embedding)
vector_index.save_local('faiss_store')


# FAISS.load_local("faiss_store", CohereEmbeddings())


# Save the index using pickle
# with open('openai_vector_index.pkl', 'wb') as f:
#     pickle.dump(vector_index, f)

# print("Index saved successfully!")

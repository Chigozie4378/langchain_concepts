#============= Vector Embeddings ============
# Load csv file with pandas
import pandas as pd
pd.set_option('display.max_colwidth',100)
data = pd.read_csv('data.csv')

# vectorize data for embedding
from sentence_transformers import SentenceTransformer
encoder = SentenceTransformer('all-mpnet-base-v2')
vector = encoder.encode(data.text)

# get the dimension of the vectorized data for the vector db
dim = vector.shape[1]

# Create FAISS index for similarity search
import faiss
index = faiss.IndexFlatL2(dim)

# add vectors to the index
index.add(vector)

while True:
    search_query = input('Search away: ')
    if not search_query.strip():
        print("Empty query. Please enter a valid search term.")
        continue
    vectorized_query = encoder.encode([search_query])
    distance, indices = index.search(vectorized_query, k=3)
    results = data.iloc[indices[0]]
    print("Search results:")
    print(f"Text: {results}")
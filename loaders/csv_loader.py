# CSV Loader
from langchain_community.document_loaders.csv_loader import CSVLoader
loader2 = CSVLoader('DIM_Calender.csv',source_column='Date')
data2 = loader2.load()
print(data2[0].metadata)
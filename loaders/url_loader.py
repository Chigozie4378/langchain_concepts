# Unstructure Url Loader
from langchain_community.document_loaders import UnstructuredURLLoader
loader = UnstructuredURLLoader(urls=[
    'https://www.moneycontrol.com/news/business/markets/stock-radar-awfis-space-solutions-kfin-technologies-tata-steel-cummins-india-cesc-in-focus-on-thursday-12736117.html',
    'https://www.moneycontrol.com/news/business/markets/us-markets-decline-while-treasury-yields-edge-higher-s-gift-nifty-down-12736065.html',
    'https://www.bbc.co.uk/sport/articles/c9eep4zlljpo',
    'https://www.premierleague.com/match/93586'
])
url_data = loader.load()
print(url_data[0].page_content)
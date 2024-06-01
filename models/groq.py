from langchain_groq import ChatGroq
from key import grok_api_key
llm = ChatGroq(api_key=grok_api_key)
#================OpenAI api
def openai_model():
    from key import openai_api_key
    from langchain_openai import OpenAI
    llm = OpenAI(api_key=openai_api_key, temperature=0.6)
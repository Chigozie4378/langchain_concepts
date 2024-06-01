import warnings
warnings.filterwarnings('ignore') 

from key import cohere_api_key
from langchain_community.chat_models import ChatCohere

class CustomChatCohere(ChatCohere):
    def _get_generation_info(self, response):
        # Custom handling of generation info
        generation_info = {}
        if hasattr(response, 'token_count'):
            generation_info["token_count"] = response.token_count
        # Add other attributes if needed
        return generation_info

llm = CustomChatCohere(cohere_api_key=cohere_api_key)

# ===================== SEQUENTIAL CHAIN USING RUNNABLE SEQUENCE ======================
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence

cuisine = input('What kind of Restaurant? (e.g Asian, African, etc.): ')

template1 = 'I want to open a restaurant for {cuisine} food. Suggest only one fancy name for this restaurant'
prompt1 = ChatPromptTemplate.from_template(template1)
chain1 = prompt1 | llm

template2 = 'List possible Menus for {cuisine} Restaurant'
prompt2 = ChatPromptTemplate.from_template(template2)
chain2 = prompt2 | llm

# Sequential chain using RunnableSequence
result_chain = RunnableSequence(chain1, chain2)
result = result_chain.invoke(cuisine)
print(result)
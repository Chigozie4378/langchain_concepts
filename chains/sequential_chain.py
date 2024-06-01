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

#===================== SEQUENTIAL CHAIN USING LLMChain, SequentialChain ======================
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain, SequentialChain
cuisine = input('What kind of Restuarant? (e.g Asian, African, etc.): ')
template1 = 'I want to open a restuarant for {cuisine} food. Suggest only one fancy name for this restaurant'
prompt1 = ChatPromptTemplate.from_template(template1)
chain1 = LLMChain(llm=llm,prompt=prompt1,output_key='restaurant_name')

template2 = 'List possible Menus for {cuisine} Restaurant'
prompt2 = ChatPromptTemplate.from_template(template2)
chain2 = LLMChain(llm=llm,prompt=prompt2,output_key='restaurant_menus')

result = SequentialChain(chains = [chain1,chain2],input_variables = ['cuisine'],output_variables = ['restaurant_name','restaurant_menus']
)
print(result.invoke(cuisine))
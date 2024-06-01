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

#==================== PROMPT TEMPLATE =====================
from langchain.prompts import PromptTemplate
prompt_template = '''
I want to open a restuarant for {cuisine} food. Suggest only one fancy name for this restaurant
'''
prompt = PromptTemplate(
    input_variables=['cuisine'],
    template=prompt_template
)
print(prompt.format(cuisine='Italian'))

#===================== CHAIN ======================
#Using Runnable
chain = prompt | llm
response =chain.invoke('Chinese')
print(response.content)
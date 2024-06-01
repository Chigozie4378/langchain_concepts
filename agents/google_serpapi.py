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

from key import serp_api_key
import os
os.environ['SERPAPI_API_KEY'] = serp_api_key
from langchain.agents import AgentType, initialize_agent, load_tools
tools = load_tools(['serpapi','llm-math'],llm=llm)
agent = initialize_agent(tools,llm,agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION)
response = agent.invoke('What wa the score between inter miami and atlanta united today and who scored')
print(response['output'])
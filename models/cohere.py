#================ Cohere Model
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

# class CustomChatCohere(ChatCohere):
#     def _get_generation_info(self, response):
#         # Custom handling of generation info
#         generation_info = {}
#         if hasattr(response, 'token_count'):
#             generation_info["token_count"] = response.token_count
#         # Add other attributes if needed
#         return generation_info

#     def get_num_tokens(self, text: str) -> int:
#         # Specify the model explicitly
#         response = self.client.tokenize(text=text, model=self.model)
#         return len(response.tokens)
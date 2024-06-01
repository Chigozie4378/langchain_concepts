





#===================== MEMORY ===================

from langchain.prompts import PromptTemplate
from langchain.memory.buffer import ConversationBufferMemory
# prompt_template = '''
# Give me answers in one sentence. What is {prompt}
# '''
# prompt = PromptTemplate(
#     input_variables=['prompt'],
#     template=prompt_template
# )
# memory = ConversationBufferMemory()
# chain = prompt | llm | memory
# response =chain.invoke('thermodynamic')
# print(response.content)

# Define the prompt template
# prompt_template = '''
# Give me a {prompt}
# '''
# prompt = PromptTemplate(
#     input_variables=['prompt'],
#     template=prompt_template
# )

# Initialize the memory
# memory = ConversationBufferMemory()

# # Chain the components together
# from langchain.chains import LLMChain

# chain = LLMChain(
#     llm=llm,
#     prompt=prompt,
#     memory=memory
# )

# # Run the chain with a specific input
# response = chain.run(prompt='list of its application')

# print(chain.memory.buffer)



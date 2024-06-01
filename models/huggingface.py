#================ HuggingFace API

def huggingface_model():
    from key import huggingface_api_key
    from langchain_community.llms import HuggingFaceHub

    llm = HuggingFaceHub(
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        task="text-generation",
        huggingfacehub_api_token=huggingface_api_key,
        model_kwargs={
            "max_new_tokens": 512,
            "top_k": 30,
            "temperature": 0.1,
            "repetition_penalty": 1.03,
        },
    )
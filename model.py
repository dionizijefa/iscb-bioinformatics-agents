from smolagents import LiteLLMModel

ollama_model = LiteLLMModel(
    model_id="ollama_chat/qwq",
    api_base="http://192.168.50.184:11434",
    num_ctx=8192,  # more is better
)

from smolagents import LiteLLMModel, AzureOpenAIServerModel, OpenAIServerModel

ollama_model = LiteLLMModel(
    model_id="ollama_chat/llama3:8b",
    api_base="http://192.168.50.184:8080",
    num_ctx=20000,  # more is better
)


def create_azure_model():
    with open(key_path, "r") as key_file:
        api_key = key_file.read().strip()

    full_endpoint = ""
    return AzureOpenAIServerModel(
        model_id=model_id,
        azure_endpoint=full_endpoint,
        api_key=api_key,
        api_version=api_version,
    )

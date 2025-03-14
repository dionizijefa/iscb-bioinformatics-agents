from smolagents import AzureOpenAIServerModel, LiteLLMModel

def create_azure_model():
    with open(".key", "r") as key_file:
        api_key = key_file.read().strip()

    return AzureOpenAIServerModel(
        model_id="gpt-4o-mini",
        azure_endpoint="https://entropic-agents.openai.azure.com/",
        api_key=api_key,
        api_version="2024-12-01-preview",
    )

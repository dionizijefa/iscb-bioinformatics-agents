from smolagents import MultiStepAgent, CodeAgent

from tools import bioinformatics_tools
from model import ollama_model, create_azure_model, swiss_model
import logging

logger = logging.getLogger(__name__)


def create_multistep_agent(tools, model):
    """Create a MultiStepAgent with minimal configuration.

    Args:
        tools: List of tools the agent can use
        model: Function that generates agent's actions
        max_steps: Maximum number of steps to solve a task

    Returns:
        A configured MultiStepAgent
    """
    agent = CodeAgent(
        tools=tools,
        model=model,
        planning_interval=2,
        add_base_tools=True,
    )
    return agent


# azure_model = create_azure_model()


agent = create_multistep_agent(bioinformatics_tools, swiss_model)
result = agent.run(
    "In my ./data directory I have 2 reads and a human genome.\
                   I need to quantify the transcript abundance and run quality control"
)
print(result)

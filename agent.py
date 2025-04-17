from smolagents import CodeAgent
from tools import bioinformatics_tools
from model import create_azure_model
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
        max_steps=10,
        tools=tools,
        model=model,
        planning_interval=1,
        add_base_tools=True,
        additional_authorized_imports=["os"],
    )
    return agent


model = create_azure_model()
agent = create_multistep_agent(bioinformatics_tools, model)
result = agent.run(
    "In my ./data directory I have a pair-end read and a reference human genome. Run quality control on sequences \
    and quantify transcripts. All results and processing steps should be sent to the parent ./results dir"
)
print(result)

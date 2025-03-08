from smolagents import MultiStepAgent

from tools import bioinformatics_tools
from model import ollama_model
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
    agent = MultiStepAgent(tools=tools, model=model, max_steps=20, planning_interval=3)
    return agent


agent = create_multistep_agent(bioinformatics_tools, ollama_model)
result = agent.run("Respond with a hello please!")

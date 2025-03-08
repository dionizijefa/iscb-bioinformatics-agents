from smolagent import MultiStepAgent
from smolagent.agents import LogLevel
import logging

logger = logging.getLogger(__name__)


def create_multistep_agent(tools, model, max_steps=20):
    """Create a MultiStepAgent with minimal configuration.

    Args:
        tools: List of tools the agent can use
        model: Function that generates agent's actions
        max_steps: Maximum number of steps to solve a task

    Returns:
        A configured MultiStepAgent
    """
    agent = MultiStepAgent(
        tools=tools, model=model, max_steps=20, verbosity_level=LogLevel.INFO
    )
    return agent


# Example usage:
# tools = [tool1, tool2, tool3]
# agent = create_multistep_agent(tools, model_function)
# result = agent.run("Solve this problem...")

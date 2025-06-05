from google.adk.agents import SequentialAgent, LoopAgent

from .writer import outline_writer_agent
from .critic import outline_critic_agent
from .refiner import outline_refiner_agent

MODEL = "gemini-2.0-flash"

# Writes an outline based on research context and iteratively refines it
# using a critic agent.
refine_outline_loop = LoopAgent(
    name="OutlineLoopAgent",
    description="Iteratively refine the outline based on research context.",
    sub_agents=[outline_critic_agent, outline_refiner_agent],
    max_iterations=5,
)

# Overall coordinator agent that manages the outline creation process.
outline_agent = SequentialAgent(
    name="OutlineAgent",
    sub_agents=[outline_writer_agent, refine_outline_loop],
)

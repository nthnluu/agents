from google.adk.agents import SequentialAgent, LoopAgent

from .subagents.research import research_agent
from .subagents.outline import outline_agent

# Overall coordinator agent that manages the research and outline drafting process.
coordinator = SequentialAgent(
    name="ScriptDraftingAgent",
    description="Research, outline, and create a draft of a video script given a topic.",
    sub_agents=[research_agent, outline_agent],
)

root_agent = coordinator

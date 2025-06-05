from google.adk import Agent

from . import prompt

MODEL = "gemini-2.0-flash"

outline_critic_agent = Agent(
    model=MODEL,
    name="OutlineCriticAgent",
    instruction=prompt.OUTLINE_CRITIC_AGENT_PROMPT,
    output_key="outline_critique",
)
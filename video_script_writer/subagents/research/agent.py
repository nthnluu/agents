from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.0-flash"

research_agent = Agent(
    model=MODEL,
    name="ResearchAgent",
    instruction=prompt.RESEARCH_AGENT_PROMPT,
    tools=[google_search],
    output_key="research_context",
)

from google.adk import Agent

from . import prompt

MODEL = "gemini-2.0-flash"

outline_writer_agent = Agent(
    model=MODEL,
    name="OutlineWriterAgent",
    instruction=prompt.OUTLINE_WRITER_AGENT_PROMPT,
    output_key="outline",
)
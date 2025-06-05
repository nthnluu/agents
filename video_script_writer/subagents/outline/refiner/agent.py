from google.adk import Agent
from google.adk.tools.tool_context import ToolContext

from . import prompt

MODEL = "gemini-2.0-flash"


def exit_loop(tool_context: ToolContext):
    """Call this function ONLY when the critique indicates no further changes are needed, signaling the iterative process should end."""
    print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    # Return empty dict as tools should typically return JSON-serializable output
    return {}


outline_refiner_agent = Agent(
    model=MODEL,
    name="OutlineRefinerAgent",
    description="This agent refines the outline based on feedback from the OutlineCriticAgent. It iteratively improves the outline until it meets the quality standards.",
    instruction=prompt.OUTLINE_REFINER_AGENT_PROMPT,
    output_key="outline",
    tools=[exit_loop],
)

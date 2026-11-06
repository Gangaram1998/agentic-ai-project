from llm_client import ask_llm
from state import AgentState

def create_plan(state:AgentState)->list[str]:

    prompt =f"""
        Goal: {state.query}
        Return 3 to 5 executable steps
        Use tools only when required.
    """

    response = ask_llm([
        {
            "role": "user",
            "content": prompt
        }
    ])

    print("response", response)

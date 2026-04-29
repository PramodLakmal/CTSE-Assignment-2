import json
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

from tools.pm_tool import write_spec_file
# TODO: Import Designer, Developer, and QA tools here

llm = ChatOllama(model="qwen2.5-coder", temperature=0.2)

def product_manager_node(state: dict) -> dict:
    """Agent 1: Translates user idea into technical spec."""
    idea = state["app_idea"]
    print(f"--- [Agent 1: PM] Gathering requirements for: {idea} ---")
    
    prompt = SystemMessage(content=(
        "You are an elite Product Manager. Create a concise technical specification "
        "for the requested web application. Include layout structure, color palette, "
        "and Javascript logic requirements."
    ))
    human_msg = HumanMessage(content=f"Idea: {idea}")
    
    try:
        response = llm.invoke([prompt, human_msg])
        spec = response.content.strip()
    except Exception as e:
        spec = f"Fallback Spec due to LLM error: {e}"
        
    # Use Tool
    write_spec_file(idea, spec)
    return {"technical_spec": spec}

def designer_node(state: dict) -> dict:
    """Agent 2: Writes the CSS based on the spec."""
    # TODO: Implement Designer Agent
    pass

def developer_node(state: dict) -> dict:
    """Agent 3: Writes HTML/JS logic."""
    # TODO: Implement Developer Agent
    pass

def qa_tester_node(state: dict) -> dict:
    """Agent 4: Audits the final code."""
    # TODO: Implement QA Tester Agent
    pass

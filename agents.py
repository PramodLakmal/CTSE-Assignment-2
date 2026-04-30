import json
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

from tools.pm_tool import write_spec_file
from tools.dev_tool import generate_application
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
    print("--- [Agent 3: Developer] Writing HTML and JS logic ---")
    spec = state["technical_spec"]
    css = state.get("css_design", "")
    
    prompt = SystemMessage(content=(
        "You are a Senior Frontend Developer. Write the complete, fully functional index.html file "
        "including all necessary HTML structure and Javascript logic to perfectly satisfy the spec. "
        "CRITICAL: Do NOT use placeholders like '// Add logic here'. You must write the actual working Javascript code to make the app fully functional. "
        "CRITICAL: You must link the stylesheet inside the <head> using <link rel='stylesheet' href='style.css'>. "
        "Output ONLY the raw HTML code."
    ))
    human_msg = HumanMessage(content=f"Spec:\n{spec}\n\nExisting CSS:\n{css}")
    
    response = llm.invoke([prompt, human_msg])
    html_content = response.content.strip()
    
    generate_application(html_content)
    return {"html_js_code": html_content}

def qa_tester_node(state: dict) -> dict:
    """Agent 4: Audits the final code."""
    # TODO: Implement QA Tester Agent
    pass

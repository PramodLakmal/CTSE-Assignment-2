import logging
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, START, END

from agents import (
    product_manager_node,
    designer_node,
    developer_node,
    qa_tester_node
)

# Observability setup
logging.basicConfig(
    filename='factory_execution.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("SoftwareFactory")

# Global State definition
class FactoryState(TypedDict):
    app_idea: str
    technical_spec: Optional[str]
    css_design: Optional[str]
    html_js_code: Optional[str]
    qa_status: Optional[dict]

# Custom wrappers to log inputs and outputs
def wrap_node_with_logging(node_func, node_name):
    def wrapped_node(state: FactoryState):
        logger.info(f"--- Entering {node_name} ---")
        result = node_func(state)
        logger.info(f"Output Delta: {str(result)[:500]}...") # truncate for sanity
        logger.info(f"--- Exiting {node_name} ---\n")
        return result
    return wrapped_node

def main():
    print("Initializing Autonomous Software Factory...")
    
    workflow = StateGraph(FactoryState)
    
    workflow.add_node("PM", wrap_node_with_logging(product_manager_node, "ProductManager"))
    workflow.add_node("Designer", wrap_node_with_logging(designer_node, "UXDesigner"))
    workflow.add_node("Developer", wrap_node_with_logging(developer_node, "FrontendDeveloper"))
    workflow.add_node("QA", wrap_node_with_logging(qa_tester_node, "QATester"))
    
    workflow.add_edge(START, "PM")
    workflow.add_edge("PM", "Designer")
    workflow.add_edge("Designer", "Developer")
    workflow.add_edge("Developer", "QA")
    workflow.add_edge("QA", END)
    
    app = workflow.compile()
    
    app_idea = "A minimalist to-do list app with smooth animations."
    print(f"\n[USER PROMPT]: {app_idea}")
    logger.info(f"STARTING FULL RUN FOR IDEA: {app_idea}")
    
    initial_state = {"app_idea": app_idea}
    
    try:
        final_state = app.invoke(initial_state)
        print("\n--- FACTORY EXECUTION COMPLETE ---")
        print("QA Audit Score:", final_state.get('qa_status', {}).get('audit', {}).get('score'))
        print("QA Statement:", final_state.get('qa_status', {}).get('statement'))
        print("\nOpen 'output_app/index.html' in your browser to view the final application!")
    except Exception as e:
        print(f"Factory failed: {e}")
        logger.error(f"Factory failed: {e}")

if __name__ == "__main__":
    main()

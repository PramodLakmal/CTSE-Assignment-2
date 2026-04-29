import os

def write_spec_file(idea: str, spec_content: str) -> str:
    """
    Writes the Product Requirements Document (PRD) to a local file.
    
    Args:
        idea (str): The original user prompt.
        spec_content (str): The detailed technical specification.
        
    Returns:
        str: Success message indicating the file path.
    """
    os.makedirs("output_app", exist_ok=True)
    filepath = os.path.join("output_app", "SPEC.md")
    
    content = f"# Product Requirements Document\n\n**Idea:** {idea}\n\n## Technical Specs\n{spec_content}"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    return f"Spec successfully written to {filepath}"

if __name__ == "__main__":
    print(write_spec_file("A calculator", "Must have dark mode and 4 operations."))

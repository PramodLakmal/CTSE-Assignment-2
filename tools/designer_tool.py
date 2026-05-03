import os

def generate_stylesheet(css_content: str) -> str:
    """
    Writes the provided CSS content to style.css.
    
    Args:
        css_content (str): The raw CSS code.
        
    Returns:
        str: Success message indicating the file path.
    """
    os.makedirs("output_app", exist_ok=True)
    filepath = os.path.join("output_app", "style.css")
    
    # Strip markdown block formatting if present
    if css_content.startswith("```css"):
        css_content = css_content[6:]
    elif css_content.startswith("```"):
        css_content = css_content[3:]
    if css_content.endswith("```"):
        css_content = css_content[:-3]
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(css_content.strip())
        
    return f"Stylesheet successfully written to {filepath}"

if __name__ == "__main__":
    print(generate_stylesheet("body { background: #000; }"))

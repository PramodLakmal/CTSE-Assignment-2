import os

def generate_application(html_content: str) -> str:
    """
    Writes the provided HTML and JS content to index.html.
    
    Args:
        html_content (str): The raw HTML code containing embedded JS.
        
    Returns:
        str: Success message indicating the file path.
    """
    os.makedirs("output_app", exist_ok=True)
    filepath = os.path.join("output_app", "index.html")
    
    # Strip markdown block formatting if present
    if html_content.startswith("```html"):
        html_content = html_content[7:]
    elif html_content.startswith("```"):
        html_content = html_content[3:]
    if html_content.endswith("```"):
        html_content = html_content[:-3]
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content.strip())
        
    return f"Application successfully written to {filepath}"

if __name__ == "__main__":
    print(generate_application("<h1>Hello World</h1>"))

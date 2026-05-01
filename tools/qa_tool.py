import os

def run_code_audit(html_path: str, css_path: str) -> dict:
    """
    Audits the generated code files for required elements and syntax completeness.
    
    Args:
        html_path (str): Path to the generated index.html.
        css_path (str): Path to the generated style.css.
        
    Returns:
        dict: A dictionary containing the audit score and a list of issues.
    """
    issues = []
    score = 100
    
    if not os.path.exists(html_path):
        return {"score": 0, "issues": ["index.html missing!"]}
    if not os.path.exists(css_path):
        return {"score": 0, "issues": ["style.css missing!"]}
        
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()
        
    # Check HTML structure
    if "<!doctype html>" not in html_content.lower():
        issues.append("Missing DOCTYPE declaration.")
        score -= 10
    if "<html" not in html_content.lower() or "</html>" not in html_content.lower():
        issues.append("Missing or incomplete <html> tags.")
        score -= 20
    if "<link" not in html_content.lower() and "style.css" not in html_content.lower():
        issues.append("CSS file is not linked in the HTML.")
        score -= 20
        
    # Check CSS structure
    if "{" not in css_content or "}" not in css_content:
        issues.append("CSS file appears empty or invalid.")
        score -= 20
        
    return {
        "score": max(0, score),
        "issues": issues,
        "status": "PASS" if score >= 80 else "FAIL"
    }

if __name__ == "__main__":
    # Test dummy execution
    print(run_code_audit("output_app/index.html", "output_app/style.css"))

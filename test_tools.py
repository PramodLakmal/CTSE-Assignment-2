import pytest
import os
import shutil
from tools.pm_tool import write_spec_file
from tools.dev_tool import generate_application

# Setup/Teardown
@pytest.fixture(autouse=True)
def run_around_tests():
    os.makedirs("output_app", exist_ok=True)
    yield

def test_write_spec_file():
    res = write_spec_file("Test App", "Spec content here.")
    assert "successfully written" in res
    assert os.path.exists("output_app/SPEC.md")

# TODO: Add tests for Designer, Developer, and QA tools here
#QA Tool Test
def test_run_code_audit():
    with open("output_app/index.html", "w") as f:
        f.write("<!DOCTYPE html><html><head><link rel='stylesheet' href='style.css'></head><body></body></html>")
    with open("output_app/style.css", "w") as f:
        f.write("body { color: red; }")
        
    audit = run_code_audit("output_app/index.html", "output_app/style.css")
    assert audit["score"] == 100
    assert audit["status"] == "PASS"
    
    with open("output_app/index.html", "w") as f:
        f.write("bad html no doctype")
        
    audit2 = run_code_audit("output_app/index.html", "output_app/style.css")
    assert audit2["score"] < 100
    assert len(audit2["issues"]) > 0

def test_generate_application():
    html = "<html><body><h1>Hi</h1></body></html>"
    res = generate_application(html)
    assert "successfully written" in res
    with open("output_app/index.html", "r") as f:
        assert f.read() == html

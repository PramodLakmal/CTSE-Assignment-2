import pytest
import os
import shutil
from tools.pm_tool import write_spec_file

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

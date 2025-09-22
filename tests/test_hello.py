"""
Test file for hello.py script.

This test verifies that the hello.py file prints 'Hello Oxford' when executed.
"""

import subprocess
import sys
import os
import pytest


def test_hello_py_exists():
    """Test that hello.py file exists in the repository."""
    assert os.path.exists("hello.py"), "hello.py file not found in the repository"


def test_hello_py_prints_hello_oxford():
    """Test that hello.py prints 'Hello Oxford' when executed."""
    try:
        # Run the hello.py file and capture output
        result = subprocess.run(
            [sys.executable, "hello.py"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Check that the script ran successfully
        assert result.returncode == 0, f"hello.py failed to run. Error: {result.stderr}"
        
        # Check that the output contains 'Hello Oxford'
        output = result.stdout.strip()
        assert output == "Hello Oxford", f"Expected 'Hello Oxford', but got: '{output}'"
        
    except subprocess.TimeoutExpired:
        pytest.fail("hello.py took too long to execute (>10 seconds)")
    except FileNotFoundError:
        pytest.fail("Python interpreter not found. Make sure Python is installed and accessible.")

def test_hello_py_prints_hello_oxford_or_hello_world():
    """Test that hello.py prints 'Hello Oxford' or 'Hello World' when executed."""
    try:
        # Run the hello.py file and capture output
        result = subprocess.run(
            [sys.executable, "hello.py"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Check that the script ran successfully
        assert result.returncode == 0, f"hello.py failed to run. Error: {result.stderr}"
        
        # Check that the output contains 'Hello Oxford' or 'Hello World'
        output = result.stdout.strip()
        assert output in ["Hello Oxford", "Hello World"], f"Expected 'Hello Oxford' or 'Hello World', but got: '{output}'"
        
    except subprocess.TimeoutExpired:
        pytest.fail("hello.py took too long to execute (>10 seconds)")
    except FileNotFoundError:
        pytest.fail("Python interpreter not found. Make sure Python is installed and accessible.")


# def test_hello_py_has_correct_content():
#     """Test that hello.py file contains the expected print statement."""
#     try:
#         with open("hello.py", "r", encoding="utf-8") as file:
#             content = file.read().strip()
            
#         # Check that the file contains a print statement with 'Hello Oxford'
#         expected_patterns = [
#             'print("Hello Oxford")',
#             "print('Hello Oxford')",
#         ]
        
#         assert any(pattern in content for pattern in expected_patterns), \
#             f"hello.py should contain print('Hello Oxford') or print(\"Hello Oxford\"). Found: {content}"
            
#     except FileNotFoundError:
#         pytest.fail("hello.py file not found")
#     except Exception as e:
#         pytest.fail(f"Error reading hello.py: {e}")


if __name__ == "__main__":
    # Allow running the test directly with: python test_hello.py
    pytest.main([__file__])
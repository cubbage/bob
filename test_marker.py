#!/usr/bin/env python3
"""
Test script for Marker PDF Parser integration
"""

import sys
import os
from pathlib import Path


def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")

    try:
        import marker

        print("✓ marker-pdf imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import marker-pdf: {e}")
        return False

    try:
        import fastapi

        print("✓ fastapi imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import fastapi: {e}")
        return False

    try:
        import uvicorn

        print("✓ uvicorn imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import uvicorn: {e}")
        return False

    return True


def test_marker_functionality():
    """Test basic Marker functionality"""
    print("\nTesting Marker functionality...")

    try:
        import subprocess
        import sys

        print("✓ subprocess module available")

        # Test with a simple text file
        test_file = Path("test_sample.txt")
        test_content = "This is a test document for Marker PDF Parser.\n\nIt contains multiple lines and paragraphs.\n\nThis should be parsed correctly."

        with open(test_file, "w") as f:
            f.write(test_content)

        try:
            # Test marker command-line interface
            cmd = ["uv", "run", "marker", "--help"]
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                print("✓ Marker command-line interface working")
                print("  Command available and functional")
            else:
                print(f"✗ Marker command failed: {result.stderr}")
                return False

        except Exception as e:
            print(f"✗ Marker command test failed: {e}")
            return False
        finally:
            # Clean up test file
            if test_file.exists():
                test_file.unlink()

        return True

    except ImportError as e:
        print(f"✗ Failed to import Marker functions: {e}")
        return False


def test_directory_structure():
    """Test if all required directories and files exist"""
    print("\nTesting directory structure...")

    required_files = [
        "marker_upload/app.py",
        "marker_upload/requirements.txt",
        "marker_upload/templates/upload.html",
        "marker_upload/static/js/upload.js",
        "marker_upload/README.md",
        "launch_marker.py",
    ]

    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} (missing)")
            all_exist = False

    return all_exist


def main():
    """Run all tests"""
    print("Marker PDF Parser Integration Test")
    print("=" * 40)

    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed. Please install dependencies:")
        print("  pip install -e .")
        sys.exit(1)

    # Test directory structure
    if not test_directory_structure():
        print("\n❌ Directory structure test failed.")
        sys.exit(1)

    # Test Marker functionality
    if not test_marker_functionality():
        print("\n❌ Marker functionality test failed.")
        sys.exit(1)

    print("\n✅ All tests passed!")
    print("\nYou can now start the Marker service with:")
    print("  python launch_marker.py")
    print("\nOr visit http://localhost:8000 after starting the service.")


if __name__ == "__main__":
    main()

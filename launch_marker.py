#!/usr/bin/env python3
"""
Launcher script for the Marker PDF Parser Upload Service
"""

import os
import sys
import subprocess
from pathlib import Path


def main():
    """Launch the Marker upload service"""

    # Change to the marker_upload directory
    marker_dir = Path(__file__).parent / "marker_upload"

    if not marker_dir.exists():
        print("Error: marker_upload directory not found!")
        print("Please ensure the marker_upload directory exists in the project root.")
        sys.exit(1)

    # Change to the marker_upload directory
    os.chdir(marker_dir)

    # Check if requirements are installed
    try:
        import marker
        import fastapi
        import uvicorn
    except ImportError as e:
        print(f"Missing dependencies: {e}")
        print("Installing requirements...")

        # Install requirements
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
        )

    # Start the server
    print("Starting Marker PDF Parser Upload Service...")
    print("Server will be available at: http://localhost:8000")
    print("Press Ctrl+C to stop the server")

    try:
        subprocess.run([sys.executable, "app.py"], check=True)
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

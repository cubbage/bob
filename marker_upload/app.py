import os
import tempfile
import shutil
from pathlib import Path
from typing import List, Optional
import json

from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import subprocess
import json
import sys

app = FastAPI(
    title="Marker PDF Parser", description="Upload and parse PDFs with Marker"
)

# Create uploads directory
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Supported file types
SUPPORTED_TYPES = {
    "application/pdf": ".pdf",
    "text/plain": ".txt",
    "application/msword": ".doc",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
    "application/vnd.ms-excel": ".xls",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
    "application/vnd.ms-powerpoint": ".ppt",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": ".pptx",
}


@app.get("/", response_class=HTMLResponse)
async def upload_page(request):
    """Main upload page"""
    return templates.TemplateResponse("upload.html", {"request": request})


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    use_llm: bool = Form(False),
    force_ocr: bool = Form(False),
    debug: bool = Form(False),
):
    """Handle file upload and parsing"""

    # Validate file type
    if file.content_type not in SUPPORTED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}. Supported types: {list(SUPPORTED_TYPES.keys())}",
        )

    # Create temporary file
    with tempfile.NamedTemporaryFile(
        delete=False, suffix=SUPPORTED_TYPES[file.content_type]
    ) as temp_file:
        # Write uploaded file to temp file
        shutil.copyfileobj(file.file, temp_file)
        temp_path = temp_file.name

    try:
        # Parse with Marker using command-line interface
        cmd = [
            "uv",
            "run",
            "marker",
            "--output_format",
            "markdown",
            "--output_dir",
            "/tmp/marker_output",
        ]

        if use_llm:
            cmd.extend(["--use_llm"])
        if force_ocr:
            cmd.extend(["--force_ocr"])
        if debug:
            cmd.extend(["--debug"])

        cmd.append(temp_path)

        # Run marker command
        result = subprocess.run(cmd, capture_output=True, text=True, cwd="/tmp")

        if result.returncode != 0:
            raise Exception(f"Marker failed: {result.stderr}")

        # Read the output file
        output_file = f"/tmp/marker_output/{Path(temp_path).stem}.md"
        if Path(output_file).exists():
            with open(output_file, "r") as f:
                result_text = f.read()
        else:
            # If no output file, use stdout
            result_text = result.stdout

        # Clean up temp file
        os.unlink(temp_path)

        return JSONResponse(
            {
                "success": True,
                "filename": file.filename,
                "content_type": file.content_type,
                "markdown": result_text,
                "options_used": {
                    "use_llm": use_llm,
                    "force_ocr": force_ocr,
                    "debug": debug,
                },
            }
        )

    except Exception as e:
        # Clean up temp file on error
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        raise HTTPException(status_code=500, detail=f"Error parsing file: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "marker-upload"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

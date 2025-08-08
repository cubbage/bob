# Bob Project

A Python project with integrated Marker PDF Parser for document processing.

## Features

- **Marker PDF Parser Integration**: Web-based interface for uploading and parsing various document formats
- **Multiple File Format Support**: PDF, Word, Excel, PowerPoint, and text files
- **Modern Web Interface**: Drag-and-drop file upload with real-time processing
- **Advanced Processing Options**: LLM enhancement, OCR, and debug modes

## Quick Start

### 1. Install Dependencies

```bash
# Using UV (recommended)
uv sync

# Or using pip
pip install -e .
```

### 2. Launch Marker Upload Service

```bash
# Using the launcher script
python launch_marker.py

# Or directly
cd marker_upload
python app.py
```

The service will be available at: http://localhost:8000

### 3. Use the Web Interface

1. Open your browser and go to http://localhost:8000
2. Drag and drop a file or click to browse
3. Select processing options (optional):
   - **Use LLM**: Improves quality (requires Google API key)
   - **Force OCR**: Better text extraction for scanned documents
   - **Debug mode**: Detailed processing information
4. Click "Parse Document" to process
5. Copy the parsed content using the copy button

## Project Structure

```
bob/
├── main.py                    # Main project entry point
├── launch_marker.py          # Marker service launcher
├── marker_upload/            # Marker PDF Parser service
│   ├── app.py               # FastAPI application
│   ├── requirements.txt     # Service dependencies
│   ├── templates/          # HTML templates
│   ├── static/             # Static files (CSS, JS)
│   └── README.md           # Service documentation
├── pyproject.toml          # Project configuration
└── README.md              # This file
```

## Supported File Types

| Format | Extensions | Description |
|--------|------------|-------------|
| PDF | .pdf | Portable Document Format |
| Word | .doc, .docx | Microsoft Word documents |
| Excel | .xls, .xlsx | Microsoft Excel spreadsheets |
| PowerPoint | .ppt, .pptx | Microsoft PowerPoint presentations |
| Text | .txt | Plain text files |

## API Usage

### Upload and Parse Document

```python
import requests

# Upload a file for parsing
files = {'file': open('document.pdf', 'rb')}
data = {
    'use_llm': 'true',      # Use LLM for better quality
    'force_ocr': 'false',   # Force OCR processing
    'debug': 'false'        # Enable debug mode
}

response = requests.post('http://localhost:8000/upload', files=files, data=data)
result = response.json()

print(result['markdown'])  # Parsed content
```

### Health Check

```python
import requests

response = requests.get('http://localhost:8000/health')
print(response.json())  # {'status': 'healthy', 'service': 'marker-upload'}
```

## Configuration

### Environment Variables

- `GOOGLE_API_KEY`: Required for LLM features (use_llm option)
- `TORCH_DEVICE`: Force specific torch device for inference

### Server Configuration

The Marker service runs on:
- Host: `0.0.0.0`
- Port: `8000`

You can modify these in `marker_upload/app.py`.

## Performance

Based on Marker's benchmarks:
- **Speed**: ~0.18 seconds per page on H100
- **Accuracy**: 95.67% heuristic score, 4.24 LLM score
- **Memory**: ~3.17GB VRAM usage

## Troubleshooting

### Common Issues

1. **Out of Memory Errors**:
   - Split large PDFs into smaller files
   - Set `TORCH_DEVICE` to CPU if needed

2. **Poor OCR Quality**:
   - Enable `force_ocr` option
   - Use `use_llm` for better results

3. **Missing Dependencies**:
   ```bash
   cd marker_upload
   pip install -r requirements.txt
   ```

### Debug Mode

Enable debug mode to get detailed processing information:
- Via web interface: Check the "Debug mode" checkbox
- Via API: Set `debug=true` parameter

## Development

### Running the Main Project

```bash
python main.py
```

### Running Marker Service

```bash
# Option 1: Using launcher
python launch_marker.py

# Option 2: Direct execution
cd marker_upload
python app.py
```

### Adding New Features

1. **New File Types**: Update `SUPPORTED_TYPES` in `marker_upload/app.py`
2. **UI Changes**: Modify `marker_upload/templates/upload.html`
3. **Functionality**: Update `marker_upload/static/js/upload.js`

## Dependencies

### Main Project
- Python 3.13+

### Marker Service
- marker-pdf: PDF parsing library
- fastapi: Web framework
- uvicorn: ASGI server
- python-multipart: File upload handling
- aiofiles: Async file operations
- jinja2: Template engine

## License

This project uses the Marker library which is licensed under GPL-3.0.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

- For Marker library issues: [Marker GitHub](https://github.com/datalab-to/marker)
- For project issues: Create an issue in this repository

# Marker PDF Parser Upload Service

A web-based interface for uploading and parsing various document formats using the [Marker](https://github.com/datalab-to/marker) library.

## Features

- **Multiple File Format Support**: PDF, Word (.doc, .docx), Excel (.xls, .xlsx), PowerPoint (.ppt, .pptx), and text files
- **Drag & Drop Interface**: Modern, responsive web interface with drag-and-drop file upload
- **Advanced Options**:
  - Use LLM for improved quality
  - Force OCR for better text extraction
  - Debug mode for detailed processing information
- **Real-time Processing**: Fast processing with progress indicators
- **Copy Results**: Easy copying of parsed content to clipboard

## Installation

1. **Install Dependencies**:
   ```bash
   cd marker_upload
   pip install -r requirements.txt
   ```

2. **Install Marker** (if not already installed):
   ```bash
   pip install marker-pdf
   ```

## Usage

### Starting the Server

```bash
cd marker_upload
python app.py
```

The server will start on `http://localhost:8000`

### API Endpoints

- `GET /` - Main upload interface
- `POST /upload` - File upload and parsing endpoint
- `GET /health` - Health check endpoint

### Upload Parameters

- `file` (required): The file to parse
- `use_llm` (optional): Use LLM for improved quality (requires Google API key)
- `force_ocr` (optional): Force OCR processing
- `debug` (optional): Enable debug mode

### Example API Usage

```python
import requests

files = {'file': open('document.pdf', 'rb')}
data = {
    'use_llm': 'true',
    'force_ocr': 'false',
    'debug': 'false'
}

response = requests.post('http://localhost:8000/upload', files=files, data=data)
result = response.json()
print(result['markdown'])
```

## Supported File Types

| Format | Extensions | MIME Type |
|--------|------------|-----------|
| PDF | .pdf | application/pdf |
| Word | .doc, .docx | application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document |
| Excel | .xls, .xlsx | application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet |
| PowerPoint | .ppt, .pptx | application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.presentationml.presentation |
| Text | .txt | text/plain |

## Configuration

### Environment Variables

- `GOOGLE_API_KEY`: Required for LLM features (use_llm option)
- `TORCH_DEVICE`: Force specific torch device for inference

### Server Configuration

The server runs on:
- Host: `0.0.0.0`
- Port: `8000`

You can modify these in `app.py`:

```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Troubleshooting

### Common Issues

1. **Out of Memory Errors**:
   - Decrease worker count
   - Split large PDFs into smaller files
   - Set `TORCH_DEVICE` to CPU if needed

2. **Poor OCR Quality**:
   - Enable `force_ocr` option
   - Use `use_llm` for better results

3. **File Type Not Supported**:
   - Check that the file extension is in the supported list
   - Ensure the MIME type is correct

### Debug Mode

Enable debug mode to get detailed processing information and save intermediate files:

```bash
# Via web interface: Check the "Debug mode" checkbox
# Via API: Set debug=true parameter
```

## Performance

Based on Marker's benchmarks:
- **Speed**: ~0.18 seconds per page on H100
- **Accuracy**: 95.67% heuristic score, 4.24 LLM score
- **Memory**: ~3.17GB VRAM usage

## Development

### Project Structure

```
marker_upload/
├── app.py              # Main FastAPI application
├── requirements.txt    # Python dependencies
├── templates/         # HTML templates
│   └── upload.html   # Main upload interface
├── static/           # Static files
│   ├── css/         # CSS stylesheets
│   └── js/          # JavaScript files
│       └── upload.js # Upload functionality
└── README.md        # This file
```

### Adding New File Types

1. Update `SUPPORTED_TYPES` in `app.py`
2. Add the MIME type and extension mapping
3. Update the HTML template to include the new format

## License

This project uses the Marker library which is licensed under GPL-3.0.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For issues with the Marker library itself, please refer to the [Marker GitHub repository](https://github.com/datalab-to/marker).

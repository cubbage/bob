# Bob - Technical Documentation

## Overview

Bob is a sophisticated text processing and colorization system that combines document parsing capabilities with advanced text pattern matching and visual styling. The project consists of two main components:

1. **Text Parser & Colorizer** - A web-based text processing application with real-time pattern matching and colorization
2. **Marker PDF Parser Service** - A FastAPI-based document processing service for PDF and document parsing

## Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Bob System Architecture                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐    ┌─────────────────────────────────┐ │
│  │   Frontend      │    │        Backend Services        │ │
│  │                 │    │                                 │ │
│  │ • bob.html      │◄──►│ • marker_upload/app.py         │ │
│  │ • Static JS/CSS │    │ • FastAPI + Uvicorn            │ │
│  │ • Real-time UI  │    │ • Marker PDF Parser            │ │
│  └─────────────────┘    └─────────────────────────────────┘ │
│                                                             │
│  ┌─────────────────┐    ┌─────────────────────────────────┐ │
│  │   Data Layer    │    │        Configuration           │ │
│  │                 │    │                                 │ │
│  │ • bob.json      │    │ • pyproject.toml              │ │
│  │ • localStorage  │    │ • UV package management        │ │
│  │ • Pattern rules │    │ • Environment configuration    │ │
│  └─────────────────┘    └─────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

#### Frontend
- **HTML5/CSS3/JavaScript** - Pure frontend implementation
- **Real-time DOM manipulation** - Dynamic UI updates
- **LocalStorage** - Client-side data persistence
- **jsPDF** - PDF generation capabilities
- **Clipboard API** - Copy/paste functionality

#### Backend
- **Python 3.13+** - Core runtime
- **FastAPI** - Modern async web framework
- **Uvicorn** - ASGI server
- **Jinja2** - Template engine
- **Marker PDF Parser** - Document processing library

#### Development & Deployment
- **UV** - Fast Python package manager
- **Subprocess** - Command-line integration
- **Temporary file handling** - Secure file processing
- **Static file serving** - Asset delivery

## Core Components

### 1. Text Parser & Colorizer (bob.html)

The main application is a sophisticated text processing system with the following features:

#### Pattern Matching Engine
- **Regex-based pattern matching** with case-insensitive support
- **Multi-word pattern support** for complex text matching
- **Priority-based rule system** with configurable order
- **Real-time preview** with immediate visual feedback

#### Colorization System
- **Dual-color styling** (color1/color2) with independent style application
- **Multiple style types**: background, text color, underline, border, symbol
- **Group-based organization** with emoji indicators
- **Object-level granularity** within groups

#### Data Management
- **Hierarchical data structure**:
  - `defaultPattern` - Global fallback pattern
  - `dictionary.rules` - Group-level patterns
  - `objectsData.objects` - Object-level patterns
  - `listsData` - Key-value lists and arrays

#### Export Capabilities
- **Markdown export** with inline HTML styling
- **PDF generation** using jsPDF
- **HTML copy** with preserved styling
- **Plain text export**
- **Shareable URLs** with embedded text and export options

### 2. Marker PDF Parser Service (marker_upload/)

A FastAPI-based service for document processing:

#### Supported Formats
- **PDF** (.pdf) - Primary target format
- **Word** (.doc, .docx) - Microsoft Word documents
- **Excel** (.xls, .xlsx) - Spreadsheet processing
- **PowerPoint** (.ppt, .pptx) - Presentation files
- **Text** (.txt) - Plain text files

#### Processing Options
- **LLM Enhancement** - Google API integration for improved quality
- **Force OCR** - Enhanced text extraction for scanned documents
- **Debug Mode** - Detailed processing information
- **Multiple output formats** - Markdown, structured text

#### API Endpoints
```python
GET  /              # Upload interface
POST /upload        # File processing endpoint
GET  /health        # Health check
```

## Data Structures

### Configuration Schema (bob.json)

```json
{
  "defaultPattern": {
    "label": "instrument",
    "color1": "#757575",
    "color2": "#ebebeb",
    "style1": "color",
    "style2": "background",
    "structure": {
      "startAnchor": false,
      "startWordBoundary": false,
      "customPrependToggles": [],
      "basePattern": ".*",
      "customAppendToggles": [],
      "endWordBoundary": false,
      "endAnchor": false
    }
  },
  "dictionary": {
    "rules": [
      {
        "match": "",
        "color1": "#A9CCE3",
        "color2": "",
        "style1": "background",
        "style2": "background",
        "label": "person",
        "enabled": true
      }
    ]
  },
  "objectsData": {
    "objects": [
      {
        "label": "Blue",
        "color1": "#457ABF",
        "color2": "",
        "style1": "color",
        "style2": "",
        "match": "blue",
        "group": "color",
        "enabled": true
      }
    ]
  },
  "listsData": {
    "keyValueLists": [
      {
        "name": "categories",
        "items": [
          {
            "key": "color",
            "value": "🎨"
          }
        ]
      }
    ],
    "arrays": [
      {
        "name": "list",
        "items": ["colors", "days of the week"]
      }
    ]
  }
}
```

## Use Cases

### 1. Document Analysis & Colorization
- **Academic research** - Color-coding different types of entities in research papers
- **Legal document processing** - Highlighting key terms, dates, and parties
- **Content analysis** - Visual pattern recognition in large text corpora
- **Educational content** - Interactive text analysis for learning

### 2. Document Processing Pipeline
- **PDF to structured text** - Converting scanned documents to searchable content
- **Multi-format support** - Processing various document types through unified interface
- **Batch processing** - Handling multiple documents with consistent formatting
- **Quality enhancement** - LLM-powered text improvement

### 3. Pattern Recognition & Visualization
- **Entity extraction** - Identifying and highlighting specific entities (people, places, dates)
- **Semantic grouping** - Organizing content by conceptual categories
- **Visual feedback** - Real-time pattern matching with immediate visual results
- **Export workflows** - Generating styled outputs for various use cases

## Development Workflow

### Local Development Setup

```bash
# 1. Install UV package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone and setup project
git clone <repository>
cd bob
uv sync

# 3. Launch services
python launch_marker.py  # Backend service
# Open bob.html in browser  # Frontend application
```

### Development Patterns

#### Frontend Development
- **Pure JavaScript** - No build process required
- **Modular functions** - Organized by feature (rules, objects, lists)
- **Event-driven architecture** - Real-time updates
- **LocalStorage persistence** - Automatic data saving

#### Backend Development
- **FastAPI async patterns** - Modern Python web development
- **Subprocess integration** - Command-line tool wrapping
- **Error handling** - Comprehensive exception management
- **File security** - Temporary file handling with cleanup

#### Configuration Management
- **UV package management** - Fast dependency resolution
- **Environment variables** - Runtime configuration
- **JSON configuration** - Structured data persistence
- **Template-based UI** - Jinja2 templating

## Performance Characteristics

### Frontend Performance
- **Real-time processing** - Immediate pattern matching feedback
- **Debounced updates** - Optimized for rapid input changes
- **Efficient DOM manipulation** - Minimal re-rendering
- **LocalStorage caching** - Persistent user preferences

### Backend Performance
- **Async processing** - Non-blocking document processing
- **Memory management** - Temporary file cleanup
- **Subprocess optimization** - Efficient command-line integration
- **Static file serving** - Optimized asset delivery

### Marker PDF Parser Performance
- **Speed**: ~0.18 seconds per page on H100
- **Accuracy**: 95.67% heuristic score, 4.24 LLM score
- **Memory**: ~3.17GB VRAM usage
- **Scalability**: Supports batch processing

## Security Considerations

### File Upload Security
- **Content type validation** - Strict file type checking
- **Temporary file handling** - Secure file processing
- **Path traversal prevention** - Safe file operations
- **Error message sanitization** - Information disclosure prevention

### Frontend Security
- **LocalStorage isolation** - Client-side data separation
- **URL parameter validation** - Safe parameter handling
- **Clipboard API security** - Secure copy operations
- **XSS prevention** - Safe HTML generation

## Deployment Considerations

### Production Deployment
- **Static file hosting** - bob.html can be served from any web server
- **API service deployment** - FastAPI with Uvicorn on production ASGI server
- **Environment configuration** - Proper API key management
- **Monitoring** - Health check endpoints for service monitoring

### Development Deployment
- **Local development** - Direct file access for frontend
- **Service discovery** - Backend service on localhost:8000
- **Hot reloading** - Manual refresh for frontend changes
- **Debug mode** - Comprehensive logging and error reporting

## Extension Points

### Frontend Extensions
- **New export formats** - Additional output types
- **Enhanced pattern matching** - More complex regex capabilities
- **UI improvements** - Additional interface features
- **Integration APIs** - External service connections

### Backend Extensions
- **Additional file formats** - New document type support
- **Processing pipelines** - Multi-step document processing
- **Storage integration** - Database or cloud storage
- **Authentication** - User management and access control

### Configuration Extensions
- **Custom pattern types** - Specialized matching rules
- **Style system expansion** - Additional visual effects
- **Data source integration** - External data feeds
- **Workflow automation** - Batch processing capabilities

## Troubleshooting Guide

### Common Issues

#### Frontend Issues
- **Pattern not matching** - Check regex syntax and case sensitivity
- **Styles not applying** - Verify color format and style configuration
- **Export failures** - Check browser compatibility and permissions
- **Data persistence** - Clear localStorage if configuration corrupted

#### Backend Issues
- **File upload failures** - Verify file type and size limits
- **Processing errors** - Check Marker installation and dependencies
- **Memory issues** - Monitor VRAM usage for large documents
- **API key problems** - Verify Google API key for LLM features

#### Performance Issues
- **Slow pattern matching** - Optimize regex patterns and reduce complexity
- **Large file processing** - Split documents or use batch processing
- **Memory leaks** - Monitor temporary file cleanup
- **UI responsiveness** - Debounce rapid input changes

## Future Development Roadmap

### Short-term Enhancements
- **Enhanced pattern editor** - Visual regex builder
- **Batch processing UI** - Multiple file upload interface
- **Advanced export options** - More output formats
- **Performance optimizations** - Faster pattern matching

### Medium-term Features
- **Cloud storage integration** - Google Drive, Dropbox support
- **Collaborative features** - Shared pattern libraries
- **API documentation** - OpenAPI/Swagger integration
- **Mobile responsiveness** - Touch-friendly interface

### Long-term Vision
- **Machine learning integration** - Automated pattern discovery
- **Multi-language support** - Internationalization
- **Plugin architecture** - Extensible processing pipelines
- **Enterprise features** - User management and analytics

## Contributing Guidelines

### Code Standards
- **Python**: PEP 8 compliance, type hints, async patterns
- **JavaScript**: ES6+ features, modular organization
- **HTML/CSS**: Semantic markup, responsive design
- **Documentation**: Comprehensive docstrings and comments

### Development Process
1. **Feature branches** - Isolated development
2. **Testing** - Manual testing for UI changes
3. **Code review** - Peer review for all changes
4. **Documentation** - Update technical docs with changes

### Testing Strategy
- **Manual testing** - UI functionality verification
- **Integration testing** - API endpoint validation
- **Performance testing** - Load testing for large documents
- **Security testing** - File upload and processing validation

This technical documentation provides a comprehensive overview of the Bob project's architecture, components, and development approach. The system represents a sophisticated text processing platform that combines modern web technologies with advanced document processing capabilities.

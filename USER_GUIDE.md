# Bob - User Guide

## What is Bob?

Bob is a powerful text processing and document analysis tool that helps you transform, analyze, and visualize text in ways that make patterns and relationships visible. Think of it as a "smart highlighter" that can automatically color-code different types of information in your documents.

## What Bob Does

### 1. **Document Processing & Text Extraction**
Bob can take various document formats and extract readable text from them:
- **PDF files** (scanned documents, forms, reports)
- **Word documents** (.doc, .docx)
- **Excel spreadsheets** (.xls, .xlsx)
- **PowerPoint presentations** (.ppt, .pptx)
- **Plain text files** (.txt)

### 2. **Smart Text Colorization & Pattern Recognition**
Once you have text, Bob can automatically identify and color-code different types of information:
- **People's names** (highlighted in blue backgrounds)
- **Dates and times** (highlighted in specific colors)
- **Numbers and quantities** (each digit gets its own color)
- **Colors mentioned in text** (the word "red" gets colored red)
- **Musical instruments** (highlighted with instrument emojis)
- **School subjects** (highlighted with book emojis)
- **Sounds and textures** (highlighted with sound emojis)
- **And much more...**

### 3. **Real-time Pattern Building**
You can create your own custom patterns to highlight specific information:
- **Regex patterns** for complex text matching
- **Custom color schemes** for different categories
- **Priority-based highlighting** (most important patterns apply first)
- **Group organization** with emoji indicators

### 4. **Multiple Export Options**
After processing, you can export your colorized text in various formats:
- **Markdown** with inline HTML styling
- **PDF documents** with preserved colors
- **HTML** for web use
- **Plain text** for further processing
- **Shareable URLs** that automatically load your text and settings

## How to Use Bob

### Getting Started

#### Option 1: Document Processing (Marker Service)
1. **Start the service**: Run `python launch_marker.py`
2. **Open your browser**: Go to `http://localhost:8000`
3. **Upload a document**: Drag and drop a PDF, Word doc, or other supported file
4. **Choose processing options**:
   - **Use LLM**: For better quality (requires Google API key)
   - **Force OCR**: For scanned documents
   - **Debug mode**: For detailed processing info
5. **Click "Parse Document"**: Wait for processing to complete
6. **Copy the result**: Use the copy button to get the extracted text

#### Option 2: Text Colorization (Main Interface)
1. **Open bob.html** in your web browser
2. **Load sample text**: Click "Load Sample.md" to see an example
3. **Paste your text**: In the input area, paste any text you want to analyze
4. **Watch real-time colorization**: Text gets automatically highlighted as you type
5. **Customize patterns**: Use the tabs to modify how text gets highlighted

### Understanding the Interface

#### Main Tabs

**1. Input Text + Preview + Export**
- **Input area**: Paste or type your text here
- **Preview area**: See real-time colorization as you type
- **Export options**: Download as Markdown, PDF, or copy to clipboard
- **Shareable URLs**: Create links that automatically load your text

**2. Default Search Pattern + Groups**
- **Default pattern**: Controls how unmatched text gets highlighted
- **Groups**: Create categories like "people," "dates," "colors"
- **Objects**: Specific items within groups (e.g., "red" within "colors")
- **Priority system**: Reorder groups to control which patterns apply first

**3. Lists and Arrays Manager**
- **Key-value lists**: Store mappings like "color → 🎨"
- **Arrays**: Simple lists of items
- **Categories**: Define emoji indicators for different groups

**4. bob.json**
- **Raw configuration**: View and edit the underlying data structure
- **Import/Export**: Load or save your complete configuration

### Working with Patterns

#### Creating a New Group
1. Go to the "Default Search Pattern + Groups" tab
2. Click "+ Add Group"
3. Select a category (person, color, instrument, etc.)
4. Choose colors and styles for the group
5. The group will automatically start highlighting matching text

#### Adding Objects to Groups
1. In the "Objects" section, click "+ Add Object"
2. Enter a label (e.g., "Red")
3. Set colors and styles
4. Enter a regex pattern (e.g., "red" to match the word "red")
5. Select which group it belongs to

#### Customizing the Default Pattern
1. In the "Default Search Pattern" section
2. Build a regex pattern using the interface:
   - **^** (start anchor): Match beginning of text
   - **\b** (word boundary): Match word boundaries
   - **Base pattern**: The main regex (e.g., "[A-Z]{1,4}" for 1-4 capital letters)
   - **Custom toggles**: Add additional regex components
3. Set colors and styles for unmatched text

### Advanced Features

#### Real-time Pattern Testing
- **Current matches**: See exactly what text your patterns are matching
- **Debug mode**: Toggle to see detailed matching information
- **Live preview**: Watch changes apply immediately as you modify patterns

#### Export and Sharing
- **Markdown export**: Download with inline HTML styling
- **PDF generation**: Create PDFs with preserved colors
- **Shareable URLs**: Create links like `?text=your_text&export=markdown`
- **Clipboard integration**: Copy styled HTML or plain text

#### Bulk Operations
- **CSV import**: Load multiple objects at once using CSV format
- **Template download**: Get a CSV template for bulk loading
- **Configuration backup**: Export your complete setup to bob.json

## Practical Use Cases

### Academic Research
**Scenario**: You're analyzing research papers and want to highlight different types of information.

1. **Upload PDF**: Use the Marker service to extract text from research papers
2. **Create groups**: Set up categories like "methodology," "results," "citations"
3. **Define patterns**: Create regex patterns to match each category
4. **Color-code**: Assign different colors to each group
5. **Export**: Generate colorized versions for presentations or reports

### Legal Document Analysis
**Scenario**: You need to quickly identify key information in legal documents.

1. **Process documents**: Upload legal PDFs through the Marker service
2. **Highlight parties**: Create a "parties" group to highlight plaintiff/defendant names
3. **Mark dates**: Create a "dates" group for important deadlines and dates
4. **Identify amounts**: Create a "monetary" group for financial figures
5. **Export results**: Generate colorized versions for case analysis

### Content Analysis
**Scenario**: You're analyzing a large corpus of text for patterns.

1. **Load text**: Paste or upload your text content
2. **Create semantic groups**: Set up categories like "emotions," "actions," "entities"
3. **Build patterns**: Use regex to match different types of content
4. **Visualize patterns**: See how different elements are distributed
5. **Export insights**: Generate reports with color-coded analysis

### Educational Content
**Scenario**: You're creating interactive learning materials.

1. **Prepare text**: Load educational content into Bob
2. **Create learning categories**: Set up groups like "vocabulary," "concepts," "examples"
3. **Add visual indicators**: Use emojis and colors to make content more engaging
4. **Generate materials**: Export colorized versions for students
5. **Share interactively**: Create shareable URLs for online learning

## Tips and Tricks

### Pattern Building
- **Start simple**: Begin with basic word matching before complex regex
- **Test incrementally**: Use the "Current Matches" display to verify patterns
- **Use word boundaries**: Add `\b` to match whole words only
- **Case sensitivity**: Patterns are case-insensitive by default

### Color Management
- **Contrast matters**: Choose colors that provide good contrast with text
- **Consistency**: Use similar colors for related categories
- **Accessibility**: Consider colorblind-friendly color schemes
- **Export compatibility**: Some colors may not export perfectly to all formats

### Performance
- **Large texts**: For very long documents, process in smaller chunks
- **Complex patterns**: Avoid overly complex regex that might slow down processing
- **Browser compatibility**: Modern browsers work best with all features

### Troubleshooting
- **Patterns not matching**: Check regex syntax and case sensitivity
- **Colors not showing**: Verify color format (hex codes work best)
- **Export issues**: Try different export formats if one doesn't work
- **Data persistence**: Clear localStorage if configuration gets corrupted

## Integration Workflows

### Document Processing Pipeline
1. **Upload documents** → Marker service extracts text
2. **Copy extracted text** → Paste into Bob's main interface
3. **Apply colorization** → Set up patterns and groups
4. **Export results** → Generate colorized versions
5. **Share or archive** → Use shareable URLs or save files

### Batch Processing
1. **Process multiple documents** → Use Marker service for each
2. **Combine text** → Merge extracted content
3. **Apply consistent patterns** → Use the same configuration across documents
4. **Export individually** → Generate separate colorized versions
5. **Compare results** → Analyze patterns across documents

### Collaborative Work
1. **Share configurations** → Export bob.json files
2. **Use shareable URLs** → Create links with embedded text and settings
3. **Standardize patterns** → Agree on color schemes and categories
4. **Iterate together** → Refine patterns based on team feedback

## What Makes Bob Special

### Real-time Processing
Unlike traditional text analysis tools, Bob provides immediate visual feedback. As you type or modify patterns, you see the results instantly.

### Flexible Pattern System
Bob's hierarchical pattern system (default → groups → objects) allows for both simple and complex text matching scenarios.

### Multiple Export Options
Whether you need Markdown for documentation, PDF for reports, or HTML for web use, Bob provides the right export format.

### Document Processing Integration
The combination of document parsing (Marker) and text analysis (Bob) creates a complete workflow from raw documents to analyzed, colorized content.

### User-friendly Interface
Despite its powerful capabilities, Bob remains accessible through an intuitive web interface that doesn't require technical expertise.

Bob transforms the way you interact with text, making patterns visible and relationships clear through intelligent colorization and real-time analysis.

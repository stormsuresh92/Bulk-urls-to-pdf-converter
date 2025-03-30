# URL to PDF Converter using Python

This repository contains a Python script for converting web pages into PDF files. It utilizes the `pdfkit` library along with the external `wkhtmltopdf` tool to generate high-quality PDFs from URLs. The script offers robust error handling, customizable options, and user-friendly logging to ensure reliability and flexibility.

**Features:**
- Batch URL processing from an input text file.
- Custom header support for web requests (e.g., User-Agent customization).
- Configurable PDF generation options (e.g., enabling local file access).
- Exception handling and logging for successful and failed conversions.
- Adjustable pause intervals to prevent server overload.

**Prerequisites:**
- Python (recommended version: 3.8 or higher).
- `pdfkit` Python library.
- `wkhtmltopdf` executable installed and configured.

**How to Use:**
1. Add your URLs to `inputurls.txt`, one per line.
2. Update the path to the `wkhtmltopdf` executable in the script.
3. Run the script to convert URLs to PDFs.

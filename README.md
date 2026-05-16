# Document Converter

A simple Python-based document conversion tool using Aspose.Words for Python.

This project allows you to convert documents between supported formats such as:

- `.docx`
- `.pdf`
- `.html`
- `.odt`

The script can be run locally with Python or inside a Docker container.

---

## Project Structure

```text
document-converter/
├── convert.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Requirements

### Local Python Usage

- Python 3.11+
- pip

### Docker Usage

- Docker installed and running

---

## Installation

Clone or download the project:

```bash
git clone <your-repo-url>
cd document-converter
```

Or place the project files into a folder manually.

---

## Python Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Python Usage

Run the converter with:

```bash
python convert.py --input input.docx --output output.pdf
```

Example conversions:

```bash
python convert.py --input document.docx --output document.pdf
python convert.py --input document.docx --output document.html
python convert.py --input document.odt --output document.docx
python convert.py --input document.html --output document.pdf
```

---

## Docker Setup

Build the Docker image:

```bash
docker build -t doc-converter .
```

---

## Docker Usage

Run the converter against files in your current directory.

### Linux/macOS

```bash
docker run --rm -v "$PWD:/work" -w /work doc-converter --input input.docx --output output.pdf
```

### Windows PowerShell

```powershell
docker run --rm -v "${PWD}:/work" -w /work doc-converter --input input.docx --output output.pdf
```

This mounts your current folder into the container and runs the converter from there.

---

## Optional Wrapper Script

To avoid typing the full Docker command every time, you can create a small wrapper script.

---

### Linux/macOS Wrapper

Create a file called `convert.sh`:

```bash
#!/usr/bin/env bash

docker run --rm \
  -v "$PWD:/work" \
  -w /work \
  doc-converter \
  --input "$1" \
  --output "$2"
```

Make it executable:

```bash
chmod +x convert.sh
```

Run it:

```bash
./convert.sh input.docx output.pdf
```

---

### Windows PowerShell Wrapper

Create a file called `convert.ps1`:

```powershell
param(
    [Parameter(Mandatory=$true)]
    [string]$InputFile,

    [Parameter(Mandatory=$true)]
    [string]$OutputFile
)

docker run --rm `
    -v "${PWD}:/work" `
    -w /work `
    doc-converter `
    --input $InputFile `
    --output $OutputFile
```

Run it:

```powershell
.\convert.ps1 input.docx output.pdf
```

---

## Supported File Types

The script currently supports the following file extensions:

```text
.odt
.pdf
.html
.docx
```

Both the input and output files must use one of these extensions.

---

## Examples

Convert a Word document to PDF:

```bash
docker run --rm -v "$PWD:/work" -w /work doc-converter --input report.docx --output report.pdf
```

Convert HTML to DOCX:

```bash
docker run --rm -v "$PWD:/work" -w /work doc-converter --input page.html --output page.docx
```

Convert ODT to PDF:

```bash
docker run --rm -v "$PWD:/work" -w /work doc-converter --input notes.odt --output notes.pdf
```

---

## Error Handling

The script checks that:

- The input file exists
- The input file type is supported
- The output file type is supported
- The output directory exists

Example error cases:

```text
Input file not found
Invalid input file type detected
Invalid output file type detected
Output directory not found
```

---

## Notes

The output file does not need to already exist. The converter creates it when the conversion succeeds.

For Docker usage, make sure the file you want to convert is inside the folder you mount into the container.

The mounted working directory is `/work` inside the Docker container.

---

## Dependencies

Python dependencies are listed in `requirements.txt`.

Example:

```text
aspose-words
```

---

## Licence

This project uses Aspose.Words, which may require a licence for production use.

Without a licence, generated documents may contain evaluation watermarks or limitations.

Check Aspose's licensing terms before using this in production.

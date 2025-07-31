# CrewAI PDF Extraction

This project demonstrates how to use CrewAI for PDF extraction and analysis. It creates a crew of AI agents that work together to process PDF documents.

## Features

- PDF content extraction using PyPDFLoader
- Content analysis and summarization
- Modular agent-based architecture using CrewAI

## Requirements

- Python 3.8+
- Virtual environment
- Required packages: crewai, langchain-community, pypdf, python-dotenv

## Setup

1. Create and activate virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install crewai langchain-community pypdf python-dotenv
```

3. Create a `.env` file with your API keys (if needed)

## Usage

1. Place your PDF file in the project directory
2. Update the `pdf_path` in `pdf_extraction.py`
3. Run the script:
```powershell
python pdf_extraction.py
```

## How it Works

The project uses two specialized agents:
1. PDF Content Extractor - Responsible for extracting text from PDF documents
2. Content Analyzer - Analyzes and summarizes the extracted content

These agents work together as a crew to process PDF documents efficiently.

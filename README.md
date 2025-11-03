# Summrize

Summrize is a lightweight command-line helper that turns long-form web articles or local text files into concise summaries using Hugging Face's `t5-small` model. It wraps the Transformers summarization pipeline with a simple Click-powered interface so you can get distilled text with a single command.

## Features
- Fetches and cleans paragraph text from any publicly accessible URL
- Summarizes local `.txt` files without leaving the terminal
- Streams progress feedback while the summarizer runs
- Ships with an example dataset (`examples/morocco-history.txt`) to help you get started quickly

## Prerequisites
- Python 3.9 or newer (3.10+ recommended for the latest Transformers releases)
- A working C++ build toolchain if TensorFlow wheels for your platform are not precompiled
- Internet access the first time the summarization model is downloaded

## Installation
1. Clone the repository and enter the project folder:
   ```powershell
   git clone https://github.com/Louay1066/Summrize.git
   cd Summrize
   ```
2. (Optional but recommended) Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate
   ```
3. Install the project and its dependencies:
   ```powershell
   pip install --upgrade pip
   pip install -r requirements.txt or python setup.py develop
   pip install -e .
   ```
   > The CLI relies on `beautifulsoup4` for HTML parsing. Install it manually (`pip install beautifulsoup4`) if your environment does not already include it.

## Usage
After installation, Summrize exposes a console entry point named `Summrize`.

### Summarize a Web Page
```powershell
Summrize --url "https://en.wikipedia.org/wiki/Natural_language_processing"
```
- Downloads the page, extracts paragraph text, and prints a summary to stdout.

### Summarize a Local File
```powershell
Summrize --file examples/morocco-history.txt
```
- Reads the file, summarizes it, and prints the condensed text.

### Notes
- Long inputs may need truncation; the default `t5-small` model summarizes up to a few paragraphs effectively. Consider chunking very large documents before summarizing.
- The first run downloads the pretrained model and tokenizer, which can take a minute depending on your connection.

## Project Layout
- `Summrize/main.py` – CLI entry point, URL extraction, and summarization logic
- `requirements.txt` – Runtime dependencies
- `examples/` – Sample text for quick experimentation

## Development Tips
- Run `pip install -e .` during development to auto-pick up code changes.
- When modifying dependencies, mirror updates in both `requirements.txt` and `setup.py` metadata.
- Add tests and integrate them with your preferred runner (e.g., `pytest`) to guard against regressions.



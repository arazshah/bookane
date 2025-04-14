 # Documentation Builder

A documentation builder with HTMX and JavaScript support for RTL and Persian language content.

## Features

- RTL and Persian language support
- Crystal theme design
- Nested chapter support
- Markdown content
- Responsive design

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

- `app.py` - Flask application
- `requirements.txt` - Python dependencies
- `templates/` - HTML templates
  - `index.html` - Main template
- `content/` - Markdown content
  - `intro.md` - Introduction chapter
  - `installation/` - Installation chapter
    - `requirements.md` - Requirements subchapter
    - `steps.md` - Installation steps subchapter
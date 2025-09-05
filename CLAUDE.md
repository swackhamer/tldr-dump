# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TLDR-Dump is a Python tool that exports all tldr-pages command documentation into organized markdown files using tealdeer. The project contains scripts to generate either a single consolidated markdown file or a categorized folder structure with 4,177+ command examples.

## Project Structure

```
tldr-dump/
├── tldr_to_markdown.py              # Single file export script
├── tldr_to_markdown_categorized.py  # Categorized export script
├── tldr_pages/                      # Generated output directory
│   ├── README.md                    # Auto-generated index
│   └── [26 category folders]        # Organized command files
├── README.md                         # Project documentation
├── USAGE.md                          # Detailed usage guide
└── CATEGORIES.md                     # Categorization logic docs
```

## Common Commands

### Generate categorized markdown files
```bash
python3 tldr_to_markdown_categorized.py --index --verbose
```

### Generate single markdown file
```bash
python3 tldr_to_markdown.py
```

### Test with limited commands
```bash
python3 tldr_to_markdown_categorized.py --limit 50 --verbose --index
```

### Update tldr cache (required before running scripts)
```bash
tldr --update
```

## Key Implementation Details

### Categorization System
- The `determine_category()` function in `tldr_to_markdown_categorized.py` uses pattern matching to organize commands into 26 categories
- Priority-based categorization ensures accurate classification
- Special character handling for shell built-ins (!, $, [, etc.)

### File Naming
- Special characters are sanitized (e.g., `$` → `dollar.md`, `!` → `bang.md`)
- The `sanitize_filename()` function handles all edge cases

### Performance
- Processing all 4,177 commands takes ~2-3 minutes
- Generates ~17MB of categorized output or ~2.5MB single file
- Single-threaded implementation with progress reporting

## Dependencies
- Python 3.6+
- tealdeer (tldr client) - must be installed: `brew install tealdeer`

## Development Notes
- No external Python dependencies (uses only stdlib)
- UTF-8 encoding throughout for international command descriptions
- Error handling for missing commands with summary reporting
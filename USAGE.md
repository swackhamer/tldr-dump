# Usage Guide

This guide provides detailed instructions for using the TLDR-Dump scripts.

## Table of Contents

- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Advanced Usage](#advanced-usage)
- [Output Formats](#output-formats)
- [Troubleshooting](#troubleshooting)
- [Tips & Tricks](#tips--tricks)

## Installation

### 1. Install tealdeer

The scripts require [tealdeer](https://github.com/dbrgn/tealdeer) to fetch tldr pages.

#### macOS
```bash
brew install tealdeer
```

#### Linux
```bash
cargo install tealdeer
```

#### Windows
```bash
scoop install tealdeer
```

### 2. Update tldr cache

```bash
tldr --update
```

### 3. Clone this repository

```bash
git clone https://github.com/yourusername/tldr-dump.git
cd tldr-dump
```

## Basic Usage

### Categorized Export (Recommended)

Generate organized markdown files in category folders:

```bash
python3 tldr_to_markdown_categorized.py --index
```

This creates:
- Individual `.md` file for each command
- Organized into category folders
- Index files for navigation

### Single File Export

Generate one large markdown file with all commands:

```bash
python3 tldr_to_markdown.py
```

This creates:
- `tldr_pages.md` with all commands
- Single searchable document
- ~2.5MB file size

## Advanced Usage

### Testing with Limited Commands

Test the script with a subset of commands:

```bash
# Process only 10 commands
python3 tldr_to_markdown_categorized.py --limit 10 --verbose

# Process only 100 commands with index
python3 tldr_to_markdown_categorized.py --limit 100 --index --verbose
```

### Custom Output Directory

Specify where to save the files:

```bash
# Categorized output to custom directory
python3 tldr_to_markdown_categorized.py --output ~/Documents/tldr-docs --index

# Single file with custom name
python3 tldr_to_markdown.py --output ~/Documents/all-commands.md
```

### Verbose Mode

See detailed progress during processing:

```bash
python3 tldr_to_markdown_categorized.py --verbose
```

Output:
```
Fetching list of all commands...
Processing 4177 of 4177 commands...
Processing 100/4177: argocd
Processing 200/4177: aws-sns
...
```

### Regenerating Specific Categories

To regenerate only specific categories, you can modify the script or use:

```bash
# Remove existing category
rm -rf tldr_pages/git/

# Run with limit to test
python3 tldr_to_markdown_categorized.py --limit 500 --index
```

## Output Formats

### Categorized Structure

```
tldr_pages/
├── README.md                    # Main index
├── android/                     # Android tools
│   ├── README.md               # Category index
│   ├── adb.md                  # Individual command
│   └── ...
├── git/                        # Git commands
│   ├── README.md
│   ├── git.md
│   ├── git-add.md
│   └── ...
└── ...
```

### Single File Structure

```markdown
# TLDR Pages Collection

Collection of 4177 command examples from tldr-pages.

---

## command-name

Description of the command.

### Examples

**Example description**

```bash
example command
```

---
```

## Command Reference

### tldr_to_markdown_categorized.py

```bash
usage: tldr_to_markdown_categorized.py [-h] [-o OUTPUT] [-l LIMIT] [-v] [--index]

Export all tldr pages to categorized markdown files

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory (default: tldr_pages)
  -l LIMIT, --limit LIMIT
                        Limit number of commands to process (for testing)
  -v, --verbose         Show progress
  --index               Create index files for each category
```

### tldr_to_markdown.py

```bash
usage: tldr_to_markdown.py [-h] [-o OUTPUT] [-l LIMIT] [-v]

Export all tldr pages to markdown

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output markdown file (default: tldr_pages.md)
  -l LIMIT, --limit LIMIT
                        Limit number of commands to process (for testing)
  -v, --verbose         Show progress
```

## Troubleshooting

### "tldr (tealdeer) is not installed"

Install tealdeer first:
```bash
brew install tealdeer  # macOS
cargo install tealdeer # Linux/Windows
```

### "No commands found"

Update the tldr cache:
```bash
tldr --update
```

### Permission Denied

Make scripts executable:
```bash
chmod +x tldr_to_markdown.py
chmod +x tldr_to_markdown_categorized.py
```

### Unicode/Encoding Errors

The scripts use UTF-8 encoding. If you encounter issues:
```bash
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

### Out of Memory

For systems with limited memory, use the limit option:
```bash
# Process in batches
python3 tldr_to_markdown_categorized.py --limit 1000
```

## Tips & Tricks

### Search Across All Commands

Using ripgrep:
```bash
rg "pattern" tldr_pages/
```

Using grep:
```bash
grep -r "pattern" tldr_pages/
```

### Find Commands by Category

```bash
ls tldr_pages/network/
ls tldr_pages/git/
```

### Convert to Other Formats

Using pandoc to convert to HTML:
```bash
pandoc tldr_pages.md -o tldr_pages.html
```

Convert category to PDF:
```bash
pandoc tldr_pages/git/*.md -o git-commands.pdf
```

### Integration with IDEs

#### VS Code
1. Open the `tldr_pages` folder
2. Use Ctrl+P to quickly find commands
3. Use Ctrl+Shift+F to search across all files

#### Vim
```vim
:e tldr_pages/
:Rg pattern
```

### Create Custom Categories

Edit the `determine_category()` function in `tldr_to_markdown_categorized.py`:

```python
# Add custom category
if 'mycustom' in cmd_lower:
    return 'my-custom-category'
```

### Batch Processing

Process and organize multiple documentation sources:
```bash
#!/bin/bash
# Export tldr pages
python3 tldr_to_markdown_categorized.py --output docs/tldr --index

# Add other documentation
cp -r other-docs/* docs/

# Generate master index
ls docs/ > docs/index.txt
```

## Performance Considerations

- **Full export**: ~2-3 minutes for 4,177 commands
- **Memory usage**: ~100-200MB during processing
- **Disk space**: ~17MB for categorized output
- **CPU**: Single-threaded, minimal CPU usage

For faster processing on large systems:
```bash
# Use PyPy if available
pypy3 tldr_to_markdown_categorized.py --index
```

## Automation

### Cron Job

Update documentation daily:
```bash
# Add to crontab
0 2 * * * cd /path/to/tldr-dump && tldr --update && python3 tldr_to_markdown_categorized.py --index
```

### Git Hook

Auto-generate on commit:
```bash
#!/bin/bash
# .git/hooks/pre-commit
python3 tldr_to_markdown_categorized.py --index
git add tldr_pages/
```
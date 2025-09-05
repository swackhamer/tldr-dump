# TLDR-Dump

A Python tool to export all [tldr-pages](https://tldr.sh/) command examples into organized markdown files. This tool uses [tealdeer](https://github.com/dbrgn/tealdeer) to fetch command documentation and organizes them into categorized folders for easy browsing and searching.

## Features

- 📚 Exports **4,177+ command examples** from tldr-pages
- 🗂️ Automatically categorizes commands into **26+ categories**
- 📝 Generates individual markdown files for each command
- 🔍 Creates searchable index files for navigation
- 🎯 Smart categorization based on command names and descriptions
- 💾 Two export modes: single file or categorized folders

## Quick Start

### Prerequisites

- Python 3.6+
- [tealdeer](https://github.com/dbrgn/tealdeer) installed (`brew install tealdeer` on macOS)

### Installation

```bash
git clone https://github.com/yourusername/tldr-dump.git
cd tldr-dump
```

### Basic Usage

#### Export to categorized folders (recommended):
```bash
python3 tldr_to_markdown_categorized.py --index
```

#### Export to a single file:
```bash
python3 tldr_to_markdown.py
```

## Output Structure

When using the categorized export, the tool creates the following structure:

```
tldr_pages/
├── README.md                 # Main index with all categories
├── git/                      # Git commands (191 files)
│   ├── README.md            # Category index
│   ├── git.md
│   ├── git-add.md
│   └── ...
├── file-operations/          # File/directory commands (525 files)
├── network/                  # Network tools (218 files)
├── containers/               # Docker/K8s (80 files)
├── programming/              # Language-specific (171 files)
└── ... (26 total categories)
```

## Categories

The tool automatically categorizes commands into intuitive groups:

| Category | Description | Example Commands |
|----------|-------------|------------------|
| `git` | Git version control | git, git-add, git-commit |
| `containers` | Container tools | docker, kubectl, helm |
| `cloud` | Cloud providers | aws, gcloud, az |
| `file-operations` | File management | ls, cp, mv, find |
| `network` | Networking tools | curl, wget, ssh, ping |
| `programming` | Language tools | python, node, cargo |
| `databases` | Database tools | mysql, postgres, redis |
| `security` | Security tools | gpg, openssl, ssh-keygen |

See [CATEGORIES.md](CATEGORIES.md) for the complete list.

## Command Line Options

### tldr_to_markdown_categorized.py

| Option | Description | Default |
|--------|-------------|---------|
| `-o`, `--output` | Output directory | `tldr_pages` |
| `-l`, `--limit` | Limit commands (for testing) | None (all) |
| `-v`, `--verbose` | Show progress | False |
| `--index` | Create index files | False |

### tldr_to_markdown.py

| Option | Description | Default |
|--------|-------------|---------|
| `-o`, `--output` | Output file | `tldr_pages.md` |
| `-l`, `--limit` | Limit commands (for testing) | None (all) |
| `-v`, `--verbose` | Show progress | False |

## Examples

### Test with a small subset
```bash
python3 tldr_to_markdown_categorized.py --limit 50 --verbose --index
```

### Export specific to custom directory
```bash
python3 tldr_to_markdown_categorized.py --output my-docs --index
```

### Create a single searchable file
```bash
python3 tldr_to_markdown.py -o all_commands.md
```

## Use Cases

- **Offline Documentation**: Access command examples without internet
- **Team Knowledge Base**: Share command references with your team
- **Learning Resource**: Browse commands by category to learn new tools
- **IDE Integration**: Import into your favorite markdown-capable IDE
- **Custom Documentation**: Build your own command reference system

## How It Works

1. **Fetches** all available commands using `tldr --list`
2. **Retrieves** documentation for each command via tealdeer
3. **Parses** the tldr format into structured data
4. **Categorizes** based on intelligent pattern matching
5. **Generates** clean markdown with proper formatting
6. **Organizes** into a logical folder structure

## Performance

- Processing time: ~2-3 minutes for all commands
- Output size: ~17MB for categorized, ~2.5MB for single file
- Total files: 4,200+ markdown files
- Categories: 26 automatic categories

## Contributing

Contributions are welcome! Areas for improvement:

- Additional categorization rules
- Export format options (HTML, PDF)
- Search functionality
- Command filtering options
- Performance optimizations

## License

MIT License - See [LICENSE](LICENSE) file for details

## Acknowledgments

- [tldr-pages](https://github.com/tldr-pages/tldr) - Community-driven command examples
- [tealdeer](https://github.com/dbrgn/tealdeer) - Fast tldr client in Rust

## Related Projects

- [tldr](https://tldr.sh/) - Original tldr-pages project
- [tealdeer](https://github.com/dbrgn/tealdeer) - Rust implementation of tldr
- [tldr-pdf](https://github.com/ryouaki/tldr-pdf) - PDF generation for tldr pages
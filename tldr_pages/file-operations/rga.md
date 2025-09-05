# rga

> Ripgrep wrapper with rich file type searching capabilities. More information: <https://github.com/phiresky/ripgrep-all>.

## Examples

### Search recursively for a pattern in all files in the current directory

```bash
rga regex
```

### List available adapters

```bash
rga --rga-list-adapters
```

### Change which adapters to use (e.g. ffmpeg, pandoc, poppler etc.)

```bash
rga --rga-adapters=adapter1,adapter2 regex
```

### Search for a pattern using the mime type instead of the file extension (slower)

```bash
rga --rga-accurate regex
```

### Display help

```bash
rga --help
```

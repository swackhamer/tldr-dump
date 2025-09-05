# md-to-clip

> Convert tldr-pages to Command Line Interface Pages. See also: `clip-view`. More information: <https://github.com/command-line-interface-pages/v2-tooling/tree/main/md-to-clip>.

## Examples

### Convert tldr-pages files and save into the same directories

```bash
md-to-clip path/to/page1.md path/to/page2.md ...
```

### Convert tldr-pages files and save into a specific directory

```bash
md-to-clip --output-directory path/to/directory path/to/page1.md path/to/page2.md ...
```

### Convert a tldr-page file to `stdout`

```bash
md-to-clip --no-file-save <(echo 'page-content')
```

### Convert tldr-pages files while recognizing additional placeholders from a specific config

```bash
md-to-clip --special-placeholder-config path/to/config.yaml path/to/page1.md path/to/page2.md ...
```

### Display help

```bash
md-to-clip --help
```

### Display version

```bash
md-to-clip --version
```

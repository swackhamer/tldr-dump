# exa

> A modern replacement for `ls` (List directory contents). More information: <https://github.com/ogham/exa#command-line-options>.

## Examples

### List files one per line

```bash
exa [-1|--oneline]
```

### List all files, including hidden files

```bash
exa [-a|--all]
```

### Long format list (permissions, ownership, size and modification date) of all files

```bash
exa [-l|--long] [-a|--all]
```

### List files with the largest at the top

```bash
exa [-r|--reverse] [-s|--sort] size
```

### Display a tree of files, three levels deep

```bash
exa [-l|--long] [-T|--tree] [-L|--level] 3
```

### List files sorted by modification date (oldest first)

```bash
exa [-l|--long] [-s|--sort] modified
```

### List files with their headers, icons, and Git statuses

```bash
exa [-l|--long] [-h|--header] --icons --git
```

### Don't list files mentioned in `.gitignore`

```bash
exa --git-ignore
```

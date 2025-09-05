# eza

> Modern, maintained replacement for `ls`, built on `exa`. More information: <https://github.com/eza-community/eza>.

## Examples

### List files one per line

```bash
eza [-1|--oneline]
```

### List all files, including hidden files

```bash
eza [-a|--all]
```

### Long format list (permissions, ownership, size and modification date) of all files

```bash
eza [-al|--all --long]
```

### List files with the largest at the top

```bash
eza [-r|--reverse] [-s|--sort] size
```

### Display a tree of files, three levels deep

```bash
eza [-lT|--long --tree] [-L|--level] 3
```

### List files sorted by modification date (oldest first)

```bash
eza [-l|--long] [-s|--sort] modified
```

### List files with their headers, icons, and Git statuses

```bash
eza [-lh|--long --header] --icons --git
```

### Don't list files mentioned in `.gitignore`

```bash
eza --git-ignore
```

# sd

> Intuitive find and replace. More information: <https://github.com/chmln/sd>.

## Examples

### Trim some whitespace using a `regex` (output stream: `stdout`)

```bash
echo 'lorem ipsum 23   ' | sd '\s+$' ''
```

### Replace words using capture groups (output stream: `stdout`)

```bash
echo 'cargo +nightly watch' | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'
```

### Find and replace in a specific file (output stream: `stdout`)

```bash
sd [-p|--preview] 'window.fetch' 'fetch' path/to/file.js
```

### Find and replace in all files in the current project (output stream: `stdout`)

```bash
sd 'from "react"' 'from "preact"' "$(find . -type f)"
```

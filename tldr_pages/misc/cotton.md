# cotton

> Markdown test specification runner. More information: <https://github.com/chonla/cotton>.

## Examples

### Use a specific base URL

```bash
cotton -u base_url path/to/file.md
```

### Disable certificate verification (insecure mode)

```bash
cotton -u base_url -i path/to/file.md
```

### Stop running when a test fails

```bash
cotton -u base_url -s path/to/file.md
```

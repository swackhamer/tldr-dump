# golangci-lint

> Parallelized, smart and fast Go linters runner that integrates with all major IDEs and supports YAML configuration. More information: <https://golangci-lint.run/welcome/quick-start/>.

## Examples

### Run linters in the current folder

```bash
golangci-lint run
```

### List enabled and disabled linters (Note: Disabled linters are shown last, do not mistake them for enabled ones)

```bash
golangci-lint linters
```

### Enable a specific linter for this run

```bash
golangci-lint run [-E|--enable] linter
```

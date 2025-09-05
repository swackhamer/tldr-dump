# go-doc

> View documentation for a package or symbol. More information: <https://pkg.go.dev/cmd/go#hdr-Show_documentation_for_package_or_symbol>.

## Examples

### View documentation for the current package

```bash
go doc
```

### Show package documentation and exported symbols

```bash
go doc encoding/json
```

### Show also documentation of symbols

```bash
go doc -all encoding/json
```

### Show also sources

```bash
go doc -all -src encoding/json
```

### Show a specific symbol

```bash
go doc -all -src encoding/json.Number
```

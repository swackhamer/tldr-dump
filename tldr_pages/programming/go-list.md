# go-list

> List packages or modules. More information: <https://pkg.go.dev/cmd/go#hdr-List_packages_or_modules>.

## Examples

### List packages

```bash
go list ./...
```

### List standard packages

```bash
go list std
```

### List packages in JSON format

```bash
go list -json time net/http
```

### List module dependencies and available updates

```bash
go list -m -u all
```

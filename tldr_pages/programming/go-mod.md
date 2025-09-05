# go-mod

> Module maintenance. More information: <https://pkg.go.dev/cmd/go#hdr-Module_maintenance>.

## Examples

### Initialize new module in current directory

```bash
go mod init moduleName
```

### Download modules to local cache

```bash
go mod download
```

### Add missing and remove unused modules

```bash
go mod tidy
```

### Verify dependencies have expected content

```bash
go mod verify
```

### Copy sources of all dependencies into the vendor directory

```bash
go mod vendor
```

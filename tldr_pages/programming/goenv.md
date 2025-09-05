# goenv

> Install, uninstall or switch between Golang versions. Supports version numbers like "1.16.15" or "1.22.8" etc. More information: <https://github.com/go-nv/goenv>.

## Examples

### List all available goenv commands

```bash
goenv commands
```

### Install a specific version of Golang

```bash
goenv install go_version
```

### Use a specific version of Golang in the current project

```bash
goenv local go_version
```

### Set the default Golang version

```bash
goenv global go_version
```

### List all available Golang versions and highlight the default one

```bash
goenv versions
```

### Uninstall a given Go version

```bash
goenv uninstall go_version
```

### Run an executable with the selected Go version

```bash
goenv exec go run go_version
```

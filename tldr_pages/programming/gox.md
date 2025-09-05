# gox

> Cross-compile Go programs. More information: <https://github.com/mitchellh/gox>.

## Examples

### Compile Go program in the current directory for all operating systems and architecture combinations

```bash
gox
```

### Download and compile a Go program from a remote URL

```bash
gox url_1 url_2
```

### Compile current directory for a particular operating system

```bash
gox -os="os"
```

### Compile current directory for a single operating system and architecture combination

```bash
gox -osarch="os/arch"
```

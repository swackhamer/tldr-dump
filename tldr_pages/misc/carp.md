# carp

> REPL and build tool for Carp. More information: <https://carp-lang.github.io/carp-docs/Manual.html>.

## Examples

### Start a REPL (interactive shell)

```bash
carp
```

### Start a REPL with a custom prompt

```bash
carp --prompt "> "
```

### Build a `carp` file

```bash
carp -b path/to/file.carp
```

### Build and run a file

```bash
carp -x path/to/file.carp
```

### Build a file with optimizations enabled

```bash
carp -b --optimize path/to/file.carp
```

### Transpile a file to C code

```bash
carp --generate-only path/to/file.carp
```

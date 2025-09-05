# scan-build

> Run a static analyzer over a codebase as part of performing a regular build. More information: <https://clang-analyzer.llvm.org/scan-build.html>.

## Examples

### Build and analyze the project in the current directory

```bash
scan-build make
```

### Run a command and pass all subsequent options to it

```bash
scan-build command command_arguments
```

### Display help

```bash
scan-build
```

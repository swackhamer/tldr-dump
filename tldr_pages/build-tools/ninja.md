# ninja

> A Build system designed to be fast. More information: <https://ninja-build.org/manual.html>.

## Examples

### Build in the current directory

```bash
ninja
```

### Build in the current directory, executing 4 jobs at a time in parallel

```bash
ninja -j 4
```

### Build a program in a given directory

```bash
ninja -C path/to/directory
```

### Show targets (e.g. `install` and `uninstall`)

```bash
ninja -t targets
```

### Display help

```bash
ninja -h
```

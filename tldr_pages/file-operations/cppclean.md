# cppclean

> Find unused code in C++ projects. More information: <https://github.com/myint/cppclean>.

## Examples

### Run in a project's directory

```bash
cppclean path/to/project
```

### Run on a project where the headers are in the `inc1/` and `inc2/` directories

```bash
cppclean path/to/project --include-path inc1 --include-path inc2
```

### Run on a specific file `main.cpp`

```bash
cppclean main.cpp
```

### Run on the current directory, excluding the "build" directory

```bash
cppclean . --exclude build
```

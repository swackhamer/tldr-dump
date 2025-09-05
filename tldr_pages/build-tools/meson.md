# meson

> SCons-like build system that uses Python as a front-end language and Ninja as a building backend. More information: <https://mesonbuild.com/Commands.html>.

## Examples

### Generate a C project with a given name and version

```bash
meson init [-l|--language] c [-n|--name] myproject --version 0.1
```

### Configure the `builddir` with default values

```bash
meson setup build_dir
```

### Build the project

```bash
meson compile -C path/to/build_dir
```

### Run all tests in the project

```bash
meson test
```

### Display help

```bash
meson [-h|--help]
```

### Display version

```bash
meson [-v|--version]
```

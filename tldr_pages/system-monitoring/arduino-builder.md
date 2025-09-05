# arduino-builder

> Compile arduino sketches. DEPRECATION WARNING: this tool is being phased out in favor of `arduino`. More information: <https://github.com/arduino/arduino-builder>.

## Examples

### Compile a sketch

```bash
arduino-builder -compile path/to/sketch.ino
```

### Specify the debug level (default: 5)

```bash
arduino-builder -debug-level 1..10
```

### Specify a custom build directory

```bash
arduino-builder -build-path path/to/build_directory
```

### Use a build option file, instead of specifying `-hardware`, `-tools`, etc. manually every time

```bash
arduino-builder -build-options-file path/to/build.options.json
```

### Enable verbose mode

```bash
arduino-builder -verbose true
```

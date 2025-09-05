# make

> Task runner for targets described in Makefile. Mostly used to control the compilation of an executable from source code. More information: <https://www.gnu.org/software/make/manual/make.html>.

## Examples

### Call the first target specified in the Makefile (usually named "all")

```bash
make
```

### Call a specific target

```bash
make target
```

### Call a specific target, executing 4 jobs at a time in parallel

```bash
make [-j|--jobs] 4 target
```

### Use a specific Makefile

```bash
make [-f|--file] path/to/file
```

### Execute make from another directory

```bash
make [-C|--directory] path/to/directory
```

### Force making of a target, even if source files are unchanged

```bash
make [-B|--always-make] target
```

### Override a variable defined in the Makefile

```bash
make target variable=new_value
```

### Override variables defined in the Makefile by the environment

```bash
make [-e|--environment-overrides] target
```

# kotlinc

> Kotlin compiler. More information: <https://kotlinlang.org/docs/command-line.html>.

## Examples

### Start a REPL (interactive shell)

```bash
kotlinc
```

### Compile a Kotlin file

```bash
kotlinc path/to/file.kt
```

### Compile several Kotlin files

```bash
kotlinc path/to/file1.kt path/to/file2.kt ...
```

### Execute a specific Kotlin Script file

```bash
kotlinc -script path/to/file.kts
```

### Compile a Kotlin file into a self contained jar file with the Kotlin runtime library included

```bash
kotlinc path/to/file.kt -include-runtime -d path/to/file.jar
```

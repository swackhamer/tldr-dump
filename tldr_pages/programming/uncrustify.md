# uncrustify

> C, C++, C#, D, Java and Pawn source code formatter. More information: <https://github.com/uncrustify/uncrustify>.

## Examples

### Format a single file

```bash
uncrustify -f path/to/file.cpp -o path/to/output.cpp
```

### Read filenames from `stdin`, and take backups before writing output back to the original filepaths

```bash
find . -name "*.cpp" | uncrustify -F - --replace
```

### Don't make backups (useful if files are under version control)

```bash
find . -name "*.cpp" | uncrustify -F - --no-backup
```

### Use a custom configuration file and write the result to `stdout`

```bash
uncrustify -c path/to/uncrustify.cfg -f path/to/file.cpp
```

### Explicitly set a configuration variable's value

```bash
uncrustify --set option=value
```

### Generate a new configuration file

```bash
uncrustify --update-config -o path/to/new.cfg
```

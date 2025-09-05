# unexpand

> Convert spaces to tabs. More information: <https://www.gnu.org/software/coreutils/manual/html_node/unexpand-invocation.html>.

## Examples

### Convert blanks in each file to tabs, writing to `stdout`

```bash
unexpand path/to/file
```

### Convert blanks to tabs, reading from `stdout`

```bash
unexpand
```

### Convert all blanks, instead of just initial blanks

```bash
unexpand [-a|--all] path/to/file
```

### Convert only leading sequences of blanks (overrides -a)

```bash
unexpand --first-only path/to/file
```

### Have tabs a certain number of characters apart, not 8 (enables -a)

```bash
unexpand [-t|--tabs] number path/to/file
```

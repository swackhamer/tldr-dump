# jtbl

> Utility to print JSON and JSON Lines data as a table in the terminal. More information: <https://github.com/kellyjonbrazil/jtbl>.

## Examples

### Print a table from JSON or JSON Lines input

```bash
cat file.json | jtbl
```

### Print a table and specify the column width for wrapping

```bash
cat file.json | jtbl --cols=width
```

### Print a table and truncate rows instead of wrapping

```bash
cat file.json | jtbl [-t|--truncate]
```

### Print a table and don't wrap or truncate rows

```bash
cat file.json | jtbl [-n|--no-wrap]
```

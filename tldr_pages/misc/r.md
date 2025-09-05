# r

> R language interpreter. More information: <https://www.r-project.org>.

## Examples

### Start a REPL (interactive shell)

```bash
R
```

### Start R in vanilla mode (i.e. a blank session that doesn't save the workspace at the end)

```bash
R [-v|--vanilla]
```

### Execute a file

```bash
R [-f|--file] path/to/file.R
```

### Execute an R expression and then exit

```bash
R -e expr
```

### Run R with a debugger

```bash
R [-d|--debugger] debugger
```

### Check R packages from package sources

```bash
R CMD check path/to/package_source
```

### Display version

```bash
R --version
```

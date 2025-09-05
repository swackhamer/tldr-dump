# dircolors

> Output commands to set the LS_COLOR environment variable and style `ls`, `dir`, etc. More information: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

## Examples

### Output commands to set LS_COLOR using default colors

```bash
dircolors
```

### Display each filetype with the color they would appear in `ls`

```bash
dircolors --print-ls-colors
```

### Output commands to set LS_COLOR using colors from a file

```bash
dircolors path/to/file
```

### Output commands for Bourne shell

```bash
dircolors [-b|--bourne-shell]
```

### Output commands for C shell

```bash
dircolors [-c|--c-shell]
```

### View the default colors for file types and extensions

```bash
dircolors [-p|--print-database]
```

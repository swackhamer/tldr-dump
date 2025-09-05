# guile

> Guile Scheme interpreter. More information: <https://www.gnu.org/software/guile/manual/guile.html#Invoking-Guile>.

## Examples

### Start a REPL (interactive shell)

```bash
guile
```

### Execute the script in a given Scheme file

```bash
guile script.scm
```

### Execute a Scheme expression

```bash
guile -c "expression"
```

### Listen on a port or a Unix domain socket (the default is port 37146) for remote REPL connections

```bash
guile --listen=port_or_socket
```

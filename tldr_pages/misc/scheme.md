# scheme

> MIT Scheme language interpreter and REPL (interactive shell). More information: <https://www.gnu.org/software/mit-scheme/documentation/stable/mit-scheme-user.html#Command_002dLine-Options>.

## Examples

### Start a REPL (interactive shell)

```bash
scheme
```

### Run a scheme program (with no REPL output)

```bash
scheme --quiet < script.scm
```

### Load a scheme program into the REPL

```bash
scheme --load script.scm
```

### Load scheme expressions into the REPL

```bash
scheme --eval "(define foo 'x)"
```

### Open the REPL in quiet mode

```bash
scheme --quiet
```

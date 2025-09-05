# racket

> Racket language interpreter. More information: <https://docs.racket-lang.org/reference/running-sa.html#%28part._mz-cmdline%29>.

## Examples

### Start a REPL (interactive shell)

```bash
racket
```

### Execute a Racket script

```bash
racket path/to/script.rkt
```

### Execute a Racket expression

```bash
racket [-e|--eval] "expression"
```

### Run module as a script (terminates option list)

```bash
racket [-l|--lib] module_name [-m|--main] arguments
```

### Start a REPL (interactive shell) for the `typed/racket` hashlang

```bash
racket -I typed/racket
```

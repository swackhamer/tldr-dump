# ulimit

> Get and set resource limits for user processes. It is a shell builtin hence not shell-agnostic. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-ulimit>.

## Examples

### Get the properties of all the user limits

```bash
ulimit -a
```

### Get hard limit for the number of simultaneously opened files

```bash
ulimit -H -n
```

### Get soft limit for the number of simultaneously opened files

```bash
ulimit -S -n
```

### Set max per-user process limit

```bash
ulimit -u 30
```

### Display help (Bash only)

```bash
help ulimit
```

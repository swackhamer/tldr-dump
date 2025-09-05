# gops

> List and diagnose Go processes currently running on your system. More information: <https://github.com/google/gops>.

## Examples

### Print all go processes running locally

```bash
gops
```

### Print more information about a process

```bash
gops pid
```

### Display a process tree

```bash
gops tree
```

### Print the current stack trace from a target program

```bash
gops stack pid|addr
```

### Print the current runtime memory statistics

```bash
gops memstats pid|addr
```

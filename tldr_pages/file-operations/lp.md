# lp

> Print files. More information: <https://manned.org/lp>.

## Examples

### Print the output of a command to the default printer (see `lpstat` command)

```bash
echo "test" | lp
```

### Print a file to the default printer

```bash
lp path/to/filename
```

### Print a file to a named printer (see `lpstat` command)

```bash
lp -d printer_name path/to/filename
```

### Print `n` copies of a file to the default printer

```bash
lp -n n path/to/filename
```

### Print only certain pages to the default printer (print pages 1, 3-5, and 16)

```bash
lp -P 1,3-5,16 path/to/filename
```

### Resume printing a job

```bash
lp -i job_id -H resume
```

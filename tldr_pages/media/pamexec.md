# pamexec

> Execute a shell command on each image in a Netpbm file. See also: `pamfile`, `pampick`, `pamsplit`. More information: <https://netpbm.sourceforge.net/doc/pamexec.html>.

## Examples

### Execute a shell command on each image in a Netpbm file

```bash
pamexec command path/to/image.pam
```

### Stop processing if a command terminates with a nonzero exit status

```bash
pamexec command path/to/image.pam [-c|-check]
```

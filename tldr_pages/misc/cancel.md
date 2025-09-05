# cancel

> Cancel print jobs. See also: `lp`, `lpmove`, `lpstat`. More information: <https://openprinting.github.io/cups/doc/man-cancel.html>.

## Examples

### Cancel the current job of the default printer (set with `lpoptions -d {{printer}}`)

```bash
cancel
```

### Cancel the jobs of the default printer owned by a specific [u]ser

```bash
cancel -u username
```

### Cancel the current job of a specific printer

```bash
cancel printer
```

### Cancel a specific job from a specific printer

```bash
cancel printer-job_id
```

### Cancel [a]ll jobs of all printers

```bash
cancel -a
```

### Cancel [a]ll jobs of a specific printer

```bash
cancel -a printer
```

### Cancel the current job of a specific server and then delete ([x]) job data files

```bash
cancel -h server -x
```

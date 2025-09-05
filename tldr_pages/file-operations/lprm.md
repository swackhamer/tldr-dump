# lprm

> Cancel queued print jobs of a server. See also: `lpq`. More information: <https://openprinting.github.io/cups/doc/man-lprm.html>.

## Examples

### Cancel current job on the default printer

```bash
lprm
```

### Cancel a job of a specific server

```bash
lprm -h server[:port] job_id
```

### Cancel multiple jobs with a encrypted connection to the server

```bash
lprm -E job_id1 job_id2 ...
```

### Cancel all jobs

```bash
lprm -
```

### Cancel the current job of a specific printer or class

```bash
lprm -P destination[/instance]
```

# disown

> Allow sub-processes to live beyond the shell that they are attached to. See also: `jobs` for finding job numbers. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>.

## Examples

### Disown the current job

```bash
disown
```

### Disown a specific job (run `jobs` to find the job number)

```bash
disown %job_number
```

### Disown all jobs (Bash only)

```bash
disown -a
```

### Keep job (do not disown it), but mark it so that no future SIGHUP is received on shell exit (Bash only)

```bash
disown -h %job_number
```

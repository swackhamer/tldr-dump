# wait

> Wait for a process to complete before proceeding. See also: `ps` to view information about running processes and `waitpid`. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-wait>.

## Examples

### Wait for a process to finish given its process ID (PID) and return its exit status

```bash
wait pid
```

### Wait for all processes known to the invoking shell to finish

```bash
wait
```

### Wait for a job to finish (run `jobs` to find the job number)

```bash
wait %job_number
```

### Display help

```bash
wait --help
```

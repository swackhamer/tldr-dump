# nomad

> Distributed, highly available, datacenter-aware scheduler. More information: <https://www.nomadproject.io/docs/commands/>.

## Examples

### Show the status of nodes in the cluster

```bash
nomad node status
```

### Validate a job file

```bash
nomad job validate path/to/file.nomad
```

### Plan a job for execution on the cluster

```bash
nomad job plan path/to/file.nomad
```

### Run a job on the cluster

```bash
nomad job run path/to/file.nomad
```

### Show the status of jobs currently running on the cluster

```bash
nomad job status
```

### Show the detailed status information about a specific job

```bash
nomad job status job_name
```

### Follow the logs of a specific allocation

```bash
nomad alloc logs alloc_id
```

### Show the status of storage volumes

```bash
nomad volume status
```

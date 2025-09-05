# envoy

> A PHP-based task manager for Laravel remote servers. More information: <https://laravel.com/docs/envoy>.

## Examples

### Initialize a configuration file

```bash
envoy init host_name
```

### Run a task

```bash
envoy run task_name
```

### Run a task from a specific project

```bash
envoy run --path path/to/directory task_name
```

### Run a task and continue on failure

```bash
envoy run --continue task_name
```

### Dump a task as a Bash script for inspection

```bash
envoy run --pretend task_name
```

### Connect to the specified server via SSH

```bash
envoy ssh server_name
```

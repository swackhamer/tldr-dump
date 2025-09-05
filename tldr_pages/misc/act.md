# act

> Execute GitHub Actions locally using Docker. More information: <https://manned.org/act>.

## Examples

### List the available jobs

```bash
act [-l|--list]
```

### Run the default event

```bash
act
```

### Run a specific event

```bash
act event_type
```

### Run a specific job

```bash
act [-j|--job] job_id
```

### Do [n]ot actually run the actions (i.e. a dry run)

```bash
act [-n|--dryrun]
```

### Show verbose logs

```bash
act [-v|--verbose]
```

### Run a specific workflow with the push event

```bash
act push [-W|--workflows] path/to/workflow
```

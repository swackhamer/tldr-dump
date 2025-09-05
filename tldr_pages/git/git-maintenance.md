# git-maintenance

> Run tasks to optimize Git repository data. More information: <https://git-scm.com/docs/git-maintenance>.

## Examples

### Register the current repository in the user's list of repositories to daily have maintenance run

```bash
git maintenance register
```

### Schedule maintenance tasks to run on the current repository every hour

```bash
git maintenance start
```

### Halt the background maintenance schedule for the current repository

```bash
git maintenance stop
```

### Remove the current repository from the user's maintenance repository list

```bash
git maintenance unregister
```

### Run a specific maintenance task on the current repository

```bash
git maintenance run --task commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch
```

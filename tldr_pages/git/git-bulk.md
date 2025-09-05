# git-bulk

> Execute operations on multiple Git repositories. Part of `git-extras`. More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

## Examples

### Register the current directory as a workspace

```bash
git bulk --addcurrent workspace_name
```

### Register a workspace for bulk operations

```bash
git bulk --addworkspace workspace_name /path/to/repository
```

### Clone a repository inside a specific directory, then register the repository as a workspace

```bash
git bulk --addworkspace workspace_name /path/to/parent_directory --from remote_repository_location
```

### Clone repositories from a newline-separated list of remote locations, then register them as workspaces

```bash
git bulk --addworkspace workspace_name /path/to/root/directory --from /path/to/file
```

### List all registered workspaces

```bash
git bulk --listall
```

### Run a Git command on the repositories of the current workspace

```bash
git bulk command command_arguments
```

### Remove a specific workspace

```bash
git bulk --removeworkspace workspace_name
```

### Remove all workspaces

```bash
git bulk --purge
```

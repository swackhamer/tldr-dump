# nx

> Manage `nx` workspaces. More information: <https://nx.dev/l/r/getting-started/nx-cli>.

## Examples

### Build a specific project

```bash
nx build project
```

### Test a specific project

```bash
nx test project
```

### Execute a target on a specific project

```bash
nx run project:target
```

### Execute a target on multiple projects

```bash
nx run-many --target target --projects project1,project2
```

### Execute a target on all projects in the workspace

```bash
nx run-many --target target --all
```

### Execute a target only on projects that have been changed

```bash
nx affected --target target
```

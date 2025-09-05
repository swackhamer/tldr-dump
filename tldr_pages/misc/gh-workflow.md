# gh-workflow

> List, view, and run GitHub Actions workflows. More information: <https://cli.github.com/manual/gh_workflow>.

## Examples

### Interactively select a workflow to view the latest jobs for

```bash
gh workflow view
```

### View a specific workflow in the default browser

```bash
gh workflow view id|workflow_name|filename.yml [-w|--web]
```

### Display the YAML definition of a specific workflow

```bash
gh workflow view id|workflow_name|filename.yml [-y|--yaml]
```

### Display the YAML definition for a specific Git branch or tag

```bash
gh workflow view id|workflow_name|filename.yml [-r|--ref] branch|tag_name [-y|--yaml]
```

### List workflow files (use `--all` to include disabled workflows)

```bash
gh workflow list
```

### Run a manual workflow with parameters

```bash
gh workflow run id|workflow_name|filename.yml --raw-field param1=value1 --raw-field param2=value2 ...
```

### Run a manual workflow using a specific branch or tag with JSON parameters from `stdin`

```bash
echo '{"param1": "value1", "param2": "value2", ...}' | gh workflow run id|workflow_name|filename.yml [-r|--ref] branch|tag_name
```

### Enable or disable a specific workflow

```bash
gh workflow enable|disable id|workflow_name|filename.yml
```

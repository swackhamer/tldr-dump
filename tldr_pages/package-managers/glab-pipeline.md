# glab-pipeline

> List, view, and run GitLab CI/CD pipelines. More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/index.md>.

## Examples

### View a running pipeline on the current branch

```bash
glab pipeline status
```

### View a running pipeline on a specific branch

```bash
glab pipeline status --branch branch_name
```

### Get the list of pipelines

```bash
glab pipeline list
```

### Run a manual pipeline on the current branch

```bash
glab pipeline run
```

### Run a manual pipeline on a specific branch

```bash
glab pipeline run --branch branch_name
```

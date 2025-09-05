# gitlab

> Ruby wrapper for the GitLab API. Some subcommands such as `ctl` have their own usage documentation. More information: <https://narkoz.github.io/gitlab/>.

## Examples

### Create a new project

```bash
gitlab create_project project_name
```

### Get info about a specific commit

```bash
gitlab commit project_name commit_hash
```

### Get info about jobs in a CI pipeline

```bash
gitlab pipeline_jobs project_name pipeline_id
```

### Start a specific CI job

```bash
gitlab job_play project_name job_id
```

# glab

> Work seamlessly with GitLab. Some subcommands such as `config` have their own usage documentation. More information: <https://gitlab.com/gitlab-org/cli/-/tree/main/docs/source>.

## Examples

### Clone a GitLab repository locally

```bash
glab repo clone owner/repository
```

### Create a new issue

```bash
glab issue create
```

### View and filter the open issues of the current repository

```bash
glab issue list
```

### View an issue in the default browser

```bash
glab issue view [-w|--web] issue_number
```

### Create a merge request

```bash
glab mr create
```

### View a pull request in the default web browser

```bash
glab mr view [-w|--web] pr_number
```

### Check out a specific pull request locally

```bash
glab mr checkout pr_number
```

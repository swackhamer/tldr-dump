# glab-repo

> Work with GitLab repositories. More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/repo/index.md>.

## Examples

### Create a new repository (if the repository name is not set, the default name will be the name of the current directory)

```bash
glab repo create name
```

### Clone a repository

```bash
glab repo clone owner/repository
```

### Fork and clone a repository

```bash
glab repo fork owner/repository [-c|--clone]
```

### View a repository in the default web browser

```bash
glab repo view owner/repository [-w|--web]
```

### Search some repositories in the GitLab instance

```bash
glab repo search [-s|--search] search_string
```

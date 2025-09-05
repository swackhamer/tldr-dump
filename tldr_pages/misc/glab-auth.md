# glab-auth

> Authenticate with a GitLab host. More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/auth/index.md>.

## Examples

### Log in with interactive prompt

```bash
glab auth login
```

### Log in with a token

```bash
glab auth login [-t|--token] token
```

### Check authentication status

```bash
glab auth status
```

### Log in to a specific GitLab instance

```bash
glab auth login [-h|--hostname] gitlab.example.com
```

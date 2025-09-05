# gh-auth

> Authenticate with a GitHub host. More information: <https://cli.github.com/manual/gh_auth>.

## Examples

### Log in with interactive prompt

```bash
gh auth login
```

### Log in with a token from `stdin` (created in <https://github.com/settings/tokens>)

```bash
echo your_token | gh auth login --with-token
```

### Check if you are logged in

```bash
gh auth status
```

### Log out

```bash
gh auth logout
```

### Log in with a specific GitHub Enterprise Server

```bash
gh auth login [-h|--hostname] github.example.com
```

### Refresh the session to ensure authentication credentials have the correct minimum scopes (removes additional scopes requested previously)

```bash
gh auth refresh
```

### Expand the permission scopes

```bash
gh auth refresh [-s|--scopes] repo,admin:repo_hook,admin:org,admin:public_key,admin:org_hook,...
```

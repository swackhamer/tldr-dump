# git-remote

> Manage set of tracked repositories ("remotes"). More information: <https://git-scm.com/docs/git-remote>.

## Examples

### List existing remotes with their names and URLs

```bash
git remote [-v|--verbose]
```

### Show information about a remote

```bash
git remote show remote_name
```

### Add a remote

```bash
git remote add remote_name remote_url
```

### Change the URL of a remote (use `--add` to keep the existing URL)

```bash
git remote set-url remote_name new_url
```

### Show the URL of a remote

```bash
git remote get-url remote_name
```

### Remove a remote

```bash
git remote remove remote_name
```

### Rename a remote

```bash
git remote rename old_name new_name
```

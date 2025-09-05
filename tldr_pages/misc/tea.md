# tea

> Interact with Gitea servers. More information: <https://gitea.com/gitea/tea>.

## Examples

### Log into a Gitea server

```bash
tea login add --name "name" --url "url" --token "token"
```

### Display all repositories

```bash
tea repos ls
```

### Display a list of issues

```bash
tea issues ls
```

### Display a list of issues for a specific repository

```bash
tea issues ls --repo "repository"
```

### Create a new issue

```bash
tea issues create --title "title" --body "body"
```

### Display a list of open pull requests

```bash
tea pulls ls
```

### Open the current repository in a browser

```bash
tea open
```

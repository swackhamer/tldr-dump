# gh-gist

> Work with GitHub Gists. More information: <https://cli.github.com/manual/gh_gist>.

## Examples

### Create a new Gist from one or more files

```bash
gh gist create path/to/file1 path/to/file2 ...
```

### Create a new Gist with a specific [desc]ription

```bash
gh gist create path/to/file1 path/to/file2 ... [-d|--desc] "description"
```

### Edit a Gist

```bash
gh gist edit id|url
```

### List up to 42 Gists owned by the currently logged in user

```bash
gh gist list [-L|--limit] 42
```

### View a Gist in the default browser without rendering Markdown

```bash
gh gist view id|url [-w|--web] [-r|--raw]
```

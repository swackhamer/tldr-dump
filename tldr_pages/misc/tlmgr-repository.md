# tlmgr-repository

> Manage repositories of a TeX Live installation. More information: <https://www.tug.org/texlive/doc/tlmgr.html#repository>.

## Examples

### List all configured repositories and their tags (if set)

```bash
tlmgr repository list
```

### List all packages available in a specific repository

```bash
tlmgr repository list path|url|tag
```

### Add a new repository with a specific tag (the tag is not required)

```bash
sudo tlmgr repository add path|url tag
```

### Remove a specific repository

```bash
sudo tlmgr repository remove path|url|tag
```

### Set a new list of repositories, overwriting the previous list

```bash
sudo tlmgr repository set path|url|tag#tag path|url|tag#tag ...
```

### Show the verification status of all configured repositories

```bash
tlmgr repository status
```

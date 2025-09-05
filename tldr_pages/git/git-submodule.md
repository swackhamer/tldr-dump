# git-submodule

> Inspects, updates and manages submodules. More information: <https://git-scm.com/docs/git-submodule>.

## Examples

### Install a repository's specified submodules

```bash
git submodule update --init --recursive
```

### Add a Git repository as a submodule

```bash
git submodule add repository_url
```

### Add a Git repository as a submodule at the specified directory

```bash
git submodule add repository_url path/to/directory
```

### Update every submodule to its latest commit

```bash
git submodule foreach git pull
```

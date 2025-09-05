# git-init

> Initialize a new local Git repository. More information: <https://git-scm.com/docs/git-init>.

## Examples

### Initialize a new local repository

```bash
git init
```

### Initialize a repository with the specified name for the initial branch

```bash
git init [-b|--initial-branch] branch_name
```

### Initialize a repository using SHA256 for object hashes (requires Git version 2.29+)

```bash
git init --object-format sha256
```

### Initialize a barebones repository, suitable for use as a remote over SSH

```bash
git init --bare
```

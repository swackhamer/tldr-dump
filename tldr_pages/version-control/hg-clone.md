# hg-clone

> Create a copy of an existing repository in a new directory. More information: <https://www.mercurial-scm.org/help/commands/clone>.

## Examples

### Clone a repository to a specified directory

```bash
hg clone remote_repository_source destination_path
```

### Clone a repository to the head of a specific branch, ignoring later commits

```bash
hg clone [-b|--branch] branch remote_repository_source
```

### Clone a repository with only the `.hg` directory, without checking out files

```bash
hg clone [-U|--noupdate] remote_repository_source
```

### Clone a repository to a specific revision, tag or branch, keeping the entire history

```bash
hg clone [-u|--updaterev] revision remote_repository_source
```

### Clone a repository up to a specific revision without any newer history

```bash
hg clone [-r|--rev] revision remote_repository_source
```

# git-symbolic-ref

> Read, change, or delete files that store references. More information: <https://git-scm.com/docs/git-symbolic-ref>.

## Examples

### Store a reference by a name

```bash
git symbolic-ref refs/name ref
```

### Store a reference by name, including a message with a reason for the update

```bash
git symbolic-ref -m "message" refs/name refs/heads/branch_name
```

### Read a reference by name

```bash
git symbolic-ref refs/name
```

### Delete a reference by name

```bash
git symbolic-ref [-d|--delete] refs/name
```

### For scripting, hide errors with `--quiet` and use `--short` to simplify ("refs/heads/X" prints as "X")

```bash
git symbolic-ref [-q|--quiet] --short refs/name
```

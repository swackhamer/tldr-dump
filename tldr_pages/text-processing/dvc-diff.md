# dvc-diff

> Show changes in DVC tracked file and directories. More information: <https://dvc.org/doc/command-reference/diff>.

## Examples

### Compare DVC tracked files from different Git commits, tags, and branches w.r.t the current workspace

```bash
dvc diff commit_hash/tag/branch
```

### Compare the changes in DVC tracked files from 1 Git commit to another

```bash
dvc diff revision1 revision2
```

### Compare DVC tracked files, along with their latest hash

```bash
dvc diff --show-hash commit
```

### Compare DVC tracked files, displaying the output as JSON

```bash
dvc diff --show-json --show-hash commit
```

### Compare DVC tracked files, displaying the output as Markdown

```bash
dvc diff --show-md --show-hash commit
```

# git-archive

> Create an archive of files from a tree. More information: <https://git-scm.com/docs/git-archive>.

## Examples

### Create a tar archive from the contents of the current HEAD and print it to `stdout`

```bash
git archive [-v|--verbose] HEAD
```

### Use the Zip format and report progress verbosely

```bash
git archive [-v|--verbose] --format zip HEAD
```

### Output the Zip archive to a specific file

```bash
git archive [-v|--verbose] [-o|--output] path/to/file.zip HEAD
```

### Create a tar archive from the contents of the latest commit of a specific branch

```bash
git archive [-o|--output] path/to/file.tar branch_name
```

### Use the contents of a specific directory

```bash
git archive [-o|--output] path/to/file.tar HEAD:path/to/directory
```

### Prepend a path to each file to archive it inside a specific directory

```bash
git archive [-o|--output] path/to/file.tar --prefix path/to/prepend/ HEAD
```

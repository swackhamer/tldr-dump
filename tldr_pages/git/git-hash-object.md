# git-hash-object

> Computes the unique hash key of content and optionally creates an object with specified type. More information: <https://git-scm.com/docs/git-hash-object>.

## Examples

### Compute the object ID without storing it

```bash
git hash-object path/to/file
```

### Compute the object ID and store it in the Git database

```bash
git hash-object -w path/to/file
```

### Compute the object ID specifying the object type

```bash
git hash-object -t blob|commit|tag|tree path/to/file
```

### Compute the object ID from `stdin`

```bash
cat path/to/file | git hash-object --stdin
```

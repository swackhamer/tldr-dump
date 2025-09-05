# git-apply

> Apply a patch to files and/or to the index without creating a commit. See also: `git am` which applies a patch and also creates a commit. More information: <https://git-scm.com/docs/git-apply>.

## Examples

### Print messages about the patched files

```bash
git apply [-v|--verbose] path/to/file
```

### Apply and add the patched files to the index

```bash
git apply --index path/to/file
```

### Apply a remote patch file

```bash
curl [-L|--location] https://example.com/file.patch | git apply
```

### Output diffstat for the input and apply the patch

```bash
git apply --stat --apply path/to/file
```

### Apply the patch in reverse

```bash
git apply [-R|--reverse] path/to/file
```

### Store the patch result in the index without modifying the working tree

```bash
git apply --cache path/to/file
```

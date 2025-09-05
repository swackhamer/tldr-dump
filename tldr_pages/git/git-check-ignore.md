# git-check-ignore

> Analyze and debug Git ignore/exclude (".gitignore") files. More information: <https://git-scm.com/docs/git-check-ignore>.

## Examples

### Check whether a file or directory is ignored

```bash
git check-ignore path/to/file_or_directory
```

### Check whether multiple files or directories are ignored

```bash
git check-ignore path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Use pathnames, one per line, from `stdin`

```bash
git check-ignore --stdin < path/to/file_list
```

### Do not check the index (used to debug why paths were tracked and not ignored)

```bash
git check-ignore --no-index path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Include details about the matching pattern for each path

```bash
git check-ignore [-v|--verbose] path/to/file_or_directory1 path/to/file_or_directory2 ...
```

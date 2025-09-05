# git-show-index

> Show the packed archive index of a Git repository. More information: <https://git-scm.com/docs/git-show-index>.

## Examples

### Read an IDX file for a Git packfile and dump its contents to `stdout`

```bash
git show-index path/to/file.idx
```

### Specify the hash algorithm for the index file (experimental)

```bash
git show-index --object-format sha1|sha256 path/to/file
```

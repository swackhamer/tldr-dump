# git-lfs

> Work with large files in Git repositories. More information: <https://github.com/git-lfs/git-lfs/tree/main/docs>.

## Examples

### Initialize Git LFS

```bash
git lfs install
```

### Track files that match a glob

```bash
git lfs track '*.bin'
```

### Change the Git LFS endpoint URL (useful if the LFS server is separate from the Git server)

```bash
git config [-f|--file] .lfsconfig lfs.url lfs_endpoint_url
```

### List tracked patterns

```bash
git lfs track
```

### List tracked files that have been committed

```bash
git lfs ls-files
```

### Push all Git LFS objects to the remote server (useful if errors are encountered)

```bash
git lfs push --all remote_name branch_name
```

### Fetch all Git LFS objects

```bash
git lfs fetch
```

### Replace pointer files with actual Git LFS objects

```bash
git lfs checkout
```

# git-fsck

> Verify the validity and connectivity of nodes in a Git repository index. Does not make any modifications. See also: `git gc` for cleaning up dangling blobs. More information: <https://git-scm.com/docs/git-fsck>.

## Examples

### Check the current repository

```bash
git fsck
```

### List all tags found

```bash
git fsck --tags
```

### List all root nodes found

```bash
git fsck --root
```

### Show all unreachable and dangling objects, ignore reflogs, and perform a full integrity check

```bash
git fsck --dangling --no-reflogs --unreachable --full
```

### Check connectivity only (skip object integrity verification)

```bash
git fsck --connectivity-only
```

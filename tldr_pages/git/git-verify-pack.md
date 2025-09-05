# git-verify-pack

> Verify packed Git archive files. More information: <https://git-scm.com/docs/git-verify-pack>.

## Examples

### Verify a packed Git archive file

```bash
git verify-pack path/to/pack-file
```

### Verify a packed Git archive file and show verbose details

```bash
git verify-pack [-v|--verbose] path/to/pack-file
```

### Verify a packed Git archive file and only display the statistics

```bash
git verify-pack [-s|--stat-only] path/to/pack-file
```

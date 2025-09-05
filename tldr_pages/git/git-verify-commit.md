# git-verify-commit

> Check for GPG verification of commits. If no commits are verified, nothing will be printed, regardless of options specified. More information: <https://git-scm.com/docs/git-verify-commit>.

## Examples

### Check commits for a GPG signature

```bash
git verify-commit commit_hash1 optional_commit_hash2 ...
```

### Check commits for a GPG signature and show details of each commit

```bash
git verify-commit commit_hash1 optional_commit_hash2 ... [-v|--verbose]
```

### Check commits for a GPG signature and print the raw details

```bash
git verify-commit commit_hash1 optional_commit_hash2 ... --raw
```

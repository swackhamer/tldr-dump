# protector

> Protect or unprotect branches on GitHub repositories. More information: <https://github.com/jcgay/protector>.

## Examples

### Protect branches of a GitHub repository (create branch protection rules)

```bash
protector branches_regex -repos organization/repository
```

### Use the dry run to see what would be protected (can also be used for freeing)

```bash
protector -dry-run branches_regex -repos organization/repository
```

### Free branches of a GitHub repository (delete branch protection rules)

```bash
protector -free branches_regex -repos organization/repository
```

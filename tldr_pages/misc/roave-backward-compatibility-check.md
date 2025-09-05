# roave-backward-compatibility-check

> Verify backward compatibility breaks between two versions of a PHP library. More information: <https://github.com/Roave/BackwardCompatibilityCheck>.

## Examples

### Check for breaking changes since the last tag

```bash
roave-backward-compatibility-check
```

### Check for breaking changes since a specific tag

```bash
roave-backward-compatibility-check --from=git_reference
```

### Check for breaking changes between the last tag and a specific reference

```bash
roave-backward-compatibility-check --to=git_reference
```

### Check for breaking changes and output to Markdown

```bash
roave-backward-compatibility-check --format=markdown > results.md
```

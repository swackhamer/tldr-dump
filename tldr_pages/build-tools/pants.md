# pants

> Fast, scalable, user-friendly, open-source build and developer workflow tool. More information: <https://www.pantsbuild.org/stable/docs/using-pants/command-line-help>.

## Examples

### Fix, format, and lint only uncommitted files

```bash
pants --changed-since=HEAD fix fmt lint
```

### Typecheck only uncommitted files and their dependents

```bash
pants --changed-since=HEAD --changed-dependents=transitive check
```

### Create a distributable package for the specified target

```bash
pants package path/to/directory:target-name
```

### Display help

```bash
pants help
```

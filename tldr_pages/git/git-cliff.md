# git-cliff

> A highly customizable changelog generator. More information: <https://git-cliff.org/docs/usage/args>.

## Examples

### Generate a changelog from all commits in a Git repository and save it to `CHANGELOG.md`

```bash
git cliff > CHANGELOG.md
```

### Generate a changelog from commits starting from the latest tag and print it to `stdout`

```bash
git cliff [-l|--latest]
```

### Generate a changelog from commits that belong to the current tag (use `git checkout` on a tag before this)

```bash
git cliff --current
```

### Generate a changelog from commits that do not belong to a tag

```bash
git cliff [-u|--unreleased]
```

### Write the default config file to `cliff.toml` in the current directory

```bash
git cliff [-i|--init]
```

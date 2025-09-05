# git-difftool

> Show file changes using external diff tools. Accepts the same options and arguments as `git diff`. See also: `git diff`. More information: <https://git-scm.com/docs/git-difftool>.

## Examples

### List available diff tools

```bash
git difftool --tool-help
```

### Set the default diff tool to meld

```bash
git config --global diff.tool "meld"
```

### Use the default diff tool to show staged changes

```bash
git difftool --staged
```

### Use a specific tool (opendiff) to show changes since a given commit

```bash
git difftool [-t|--tool] opendiff commit
```

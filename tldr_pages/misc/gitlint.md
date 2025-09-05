# gitlint

> Git commit message linter checks your commit messages for style. More information: <https://jorisroovers.com/gitlint/>.

## Examples

### Check the last commit message

```bash
gitlint
```

### The range of commits to lint

```bash
gitlint --commits single_refspec_argument
```

### Path to a directory or Python module with extra user-defined rules

```bash
gitlint --extra-path path/to/directory
```

### Start a specific CI job

```bash
gitlint --target path/to/target_directory
```

### Path to a file containing a commit-msg

```bash
gitlint --msg-filename path/to/filename
```

### Read staged commit meta-info from the local repository

```bash
gitlint --staged
```

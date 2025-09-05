# jj-git-push

> Push to a Git remote. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-push>.

## Examples

### Push a bookmark to the given remote (defaults to `git.push` setting)

```bash
jj git push [-b|--bookmark] bookmark --remote remote
```

### Push a new bookmark

```bash
jj git push [-b|--bookmark] bookmark [-N|--allow-new]
```

### Push all tracked bookmarks

```bash
jj git push --tracked
```

### Push all bookmarks (including new bookmarks)

```bash
jj git push --all
```

### Push all bookmarks pointing to given revisions

```bash
jj git push [-r|--revisions] revset
```

### Push changes/commits by creating new bookmarks (Name format is as per `templates.git_push_bookmark` setting, defaults to `"push-" ++ change_id.short()`)

```bash
jj git push [-c|--change] revset
```

### Push a revision with the given name

```bash
jj git push --named name=revision
```

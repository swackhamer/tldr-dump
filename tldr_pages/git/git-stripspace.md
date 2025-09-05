# git-stripspace

> Read text (e.g. commit messages, notes, tags, and branch descriptions) from `stdin` and clean it into the manner used by Git. More information: <https://git-scm.com/docs/git-stripspace>.

## Examples

### Trim whitespace from a file

```bash
cat path/to/file | git stripspace
```

### Trim whitespace and Git comments from a file

```bash
cat path/to/file | git stripspace [-s|--strip-comments]
```

### Convert all lines in a file into Git comments

```bash
git stripspace [-c|--comment-lines] < path/to/file
```

# git-sed

> Replace patterns in git-controlled files using sed. Part of `git-extras`. More information: <https://manned.org/git-sed>.

## Examples

### Replace the specified text in the current repository

```bash
git sed 'find_text' 'replace_text'
```

### Replace the specified text and then commit the resulting changes with a standard commit message

```bash
git sed -c 'find_text' 'replace_text'
```

### Replace the specified text, using `regex`

```bash
git sed -f g 'find_text' 'replace_text'
```

### Replace a specific text in all files under a given directory

```bash
git sed 'find_text' 'replace_text' -- path/to/directory
```

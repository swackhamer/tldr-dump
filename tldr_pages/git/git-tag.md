# git-tag

> Create, list, delete or verify tags. A tag is a static reference to a commit. More information: <https://git-scm.com/docs/git-tag>.

## Examples

### List all tags

```bash
git tag
```

### Create a tag with the given name pointing to the current commit

```bash
git tag tag_name
```

### Create a tag with the given name pointing to a given commit

```bash
git tag tag_name commit
```

### Create an annotated tag with the given message

```bash
git tag tag_name [-m|--message] tag_message
```

### Delete the tag with the given name

```bash
git tag [-d|--delete] tag_name
```

### Get updated tags from remote

```bash
git fetch [-t|--tags]
```

### Push a tag to remote

```bash
git push origin tag tag_name
```

### List all tags whose ancestors include a given commit

```bash
git tag --contains commit
```

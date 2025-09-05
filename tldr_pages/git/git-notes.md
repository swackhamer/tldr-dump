# git-notes

> Add or inspect object notes. More information: <https://git-scm.com/docs/git-notes>.

## Examples

### List all notes and the objects they are attached to

```bash
git notes list
```

### List all notes attached to a given object (defaults to HEAD)

```bash
git notes list [object]
```

### Show the notes attached to a given object (defaults to HEAD)

```bash
git notes show [object]
```

### Append a note to a specified object (opens the default text editor)

```bash
git notes append object
```

### Append a note to a specified object, specifying the message

```bash
git notes append --message="message_text"
```

### Edit an existing note (defaults to HEAD)

```bash
git notes edit [object]
```

### Copy a note from one object to another

```bash
git notes copy source_object target_object
```

### Remove all the notes added to a specified object

```bash
git notes remove object
```

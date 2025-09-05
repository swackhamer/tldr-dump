# moe

> A WYSIWYG text editor for ISO-8859-15 encoded text. More information: <https://www.gnu.org/software/moe/moe.html>.

## Examples

### Open moe and create a backup file (file~) when saving edits

```bash
moe path/to/file
```

### Open a file as read-only

```bash
moe [-o|--read-only] path/to/file
```

### Edit a file without creating backups

```bash
moe [-B|--no-backup] path/to/file
```

### Edit a file ignoring case in searches

```bash
moe [-i|--ignore-case] path/to/file
```

### Save and Quit

```bash
<Ctrl x>
```

# rename

> Rename a file or group of files with a `regex`. WARNING: This command will overwrite files without prompting unless the dry-run option is used. Note: This page refers to the Perl version, also known as `file-rename`. More information: <https://manned.org/prename>.

## Examples

### Replace `from` with `to` in the filenames of the specified files

```bash
rename 's/from/to/' *.txt
```

### Dry-run - display which changes would occur without performing them

```bash
rename -n 's/from/to/' *.txt
```

### Change the extension

```bash
rename 's/\.old$/\.new/' *.txt
```

### Change to lowercase (use `-f` in case-insensitive filesystems)

```bash
rename [-f|--force] 'y/A-Z/a-z/' *.txt
```

### Capitalize first letter of every word in the name

```bash
rename [-f|--force] 's/\b(\w)/\U$1/g' *.txt
```

### Replace spaces with underscores

```bash
rename 's/\s+/_/g' *.txt
```

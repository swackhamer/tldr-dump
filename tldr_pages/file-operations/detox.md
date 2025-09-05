# detox

> Renames files to make them easier to work with. It removes spaces and other such annoyances like duplicate underline characters. More information: <https://manned.org/detox>.

## Examples

### Remove spaces and other undesirable characters from a file's name

```bash
detox path/to/file
```

### Show how detox would rename all the files in a directory tree

```bash
detox [-n|--dry-run] -r path/to/directory
```

### Remove spaces and other undesirable characters from all files in a directory tree

```bash
detox -r path/to/directory
```

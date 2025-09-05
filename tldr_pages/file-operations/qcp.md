# qcp

> Copy files using the default text editor to define the filenames. More information: <https://manned.org/qcp>.

## Examples

### Copy a single file (open an editor with the source filename on the left and the target filename on the right)

```bash
qcp source_file
```

### Copy multiple JPEG files

```bash
qcp *.jpg
```

### Copy files, but swap the positions of the source and the target filenames in the editor

```bash
qcp [-o|--option] swap *.jpg
```

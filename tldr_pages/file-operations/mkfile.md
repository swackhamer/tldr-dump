# mkfile

> Create empty files of any size. More information: <https://manned.org/mkfile>.

## Examples

### Create an empty file of 15 kilobytes

```bash
mkfile -n 15k path/to/file
```

### Create a file of a given size and unit (bytes, KB, MB, GB)

```bash
mkfile -n sizeb|k|m|g path/to/file
```

### Create two files of 4 megabytes each

```bash
mkfile -n 4m first_filename second_filename
```

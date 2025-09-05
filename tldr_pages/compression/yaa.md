# yaa

> Create and manipulate YAA archives. More information: <https://www.manpagez.com/man/1/yaa/>.

## Examples

### Create an archive from a directory

```bash
yaa archive -d path/to/directory -o path/to/output_file.yaa
```

### Create an archive from a file

```bash
yaa archive -i path/to/file -o path/to/output_file.yaa
```

### Extract an archive to the current directory

```bash
yaa extract -i path/to/archive_file.yaa
```

### List the contents of an archive

```bash
yaa list -i path/to/archive_file.yaa
```

### Create an archive with a specific compression algorithm

```bash
yaa archive -a algorithm -d path/to/directory -o path/to/output_file.yaa
```

### Create an archive with an 8 MB block size

```bash
yaa archive -b 8m -d path/to/directory -o path/to/output_file.yaa
```

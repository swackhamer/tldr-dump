# pax

> Archiving and copying utility. More information: <https://manned.org/pax.1p>.

## Examples

### List the contents of an archive

```bash
pax -f archive.tar
```

### List the contents of a `gzip` archive

```bash
pax -zf archive.tar.gz
```

### Create an archive from files

```bash
pax -wf target.tar path/to/file1 path/to/file2 ...
```

### Create an archive from files, using output redirection

```bash
pax -w path/to/file1 path/to/file2 ... > target.tar
```

### Extract an archive into the current directory

```bash
pax -rf source.tar
```

### Copy to a directory, while keeping the original metadata; `target/` must exist

```bash
pax -rw path/to/file1 path/to/directory1 path/to/directory2 ... target/
```

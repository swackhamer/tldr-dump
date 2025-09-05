# ar

> Create, modify, and extract from Unix archives. Typically used for static libraries (`.a`) and Debian packages (`.deb`). See also: `tar`. More information: <https://manned.org/ar>.

## Examples

### E[x]tract all members from an archive

```bash
ar x path/to/file.a
```

### Lis[t] contents in a specific archive

```bash
ar t path/to/file.ar
```

### [r]eplace or add specific files to an archive

```bash
ar r path/to/file.deb path/to/debian-binary path/to/control.tar.gz path/to/data.tar.xz ...
```

### In[s]ert an object file index (equivalent to using `ranlib`)

```bash
ar s path/to/file.a
```

### Create an archive with specific files and an accompanying object file index

```bash
ar rs path/to/file.a path/to/file1.o path/to/file2.o ...
```

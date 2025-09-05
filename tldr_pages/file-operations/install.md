# install

> Copy files and set attributes. Copy files (often executable) to a system location like `/usr/local/bin`, give them the appropriate permissions/ownership. More information: <https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>.

## Examples

### Copy files to the destination

```bash
install path/to/source_file1 path/to/source_file2 ... path/to/destination
```

### Copy files to the destination, setting their ownership

```bash
install [-o|--owner] user path/to/source_file1 path/to/source_file2 ... path/to/destination
```

### Copy files to the destination, setting their group ownership

```bash
install [-g|--group] user path/to/source_file1 path/to/source_file2 ... path/to/destination
```

### Copy files to the destination, setting their `mode`

```bash
install [-m|--mode] +x path/to/source_file1 path/to/source_file2 ... path/to/destination
```

### Copy files and apply access/modification times of source to the destination

```bash
install [-p|--preserve-timestamps] path/to/source_file1 path/to/source_file2 ... path/to/destination
```

### Copy files and create the directories at the destination if they don't exist

```bash
install -D path/to/source_file1 path/to/source_file2 ... path/to/destination
```

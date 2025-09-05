# ipfs

> Inter Planetary File System. A peer-to-peer hypermedia protocol. Aims to make the web more open. More information: <https://ipfs.io>.

## Examples

### Add a file from local to the filesystem, pin it and print the relative hash

```bash
ipfs add path/to/file
```

### Add a directory and its files recursively from local to the filesystem and print the relative hash

```bash
ipfs add -r path/to/directory
```

### Save a remote file and give it a name but not pin it

```bash
ipfs get hash -o path/to/file
```

### Pin a remote file locally

```bash
ipfs pin add hash
```

### Display pinned files

```bash
ipfs pin ls
```

### Unpin a file from the local storage

```bash
ipfs pin rm hash
```

### Remove unpinned files from local storage

```bash
ipfs repo gc
```

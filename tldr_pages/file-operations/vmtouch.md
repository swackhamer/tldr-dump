# vmtouch

> Manage the filesystem cache. More information: <https://manned.org/vmtouch>.

## Examples

### Print the cache status of a file

```bash
vmtouch path/to/file
```

### Load a file into cache

```bash
vmtouch -t path/to/file
```

### Evict a file from cache

```bash
vmtouch -e path/to/file
```

### Lock a file in cache to prevent eviction from memory

```bash
vmtouch -l path/to/file
```

### Lock a file and daemonize the program

```bash
vmtouch -ld path/to/file
```

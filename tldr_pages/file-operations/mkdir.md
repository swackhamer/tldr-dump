# mkdir

> Create directories and set their permissions. More information: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

## Examples

### Create specific directories

```bash
mkdir path/to/directory1 path/to/directory2 ...
```

### Create specific directories and their parents if needed

```bash
mkdir [-p|--parents] path/to/directory1 path/to/directory2 ...
```

### Create directories with specific permissions

```bash
mkdir [-m|--mode] rwxrw-r-- path/to/directory1 path/to/directory2 ...
```

### Create multiple nested directories recursively

```bash
mkdir [-p|--parents] path/to/{a,b}/{x,y,z}/{h,i,j}
```

# vidir

> Edit directories in a text editor. More information: <https://manned.org/vidir>.

## Examples

### Edit the contents of the specified directories

```bash
vidir path/to/directory1 path/to/directory2 ...
```

### Display each action taken by the program

```bash
vidir [-v|--verbose] path/to/directory1 path/to/directory2 ...
```

### Edit the contents of current directory

```bash
vidir
```

### Use the specified text editor

```bash
EDITOR=vim vidir path/to/directory1 path/to/directory2 ...
```

### Read a list of files to edit from `stdin`

```bash
command | vidir -
```

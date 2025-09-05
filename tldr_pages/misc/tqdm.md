# tqdm

> Show progress over time of a command. More information: <https://tqdm.github.io/docs/cli/>.

## Examples

### Show iterations per second and use `stdout` afterwards

```bash
seq 10000000 | tqdm | command
```

### Create a progress bar

```bash
seq 10000000 | tqdm --total 10000000 | command
```

### Create an archive out of a directory and use the file count of that directory to create a progress bar

```bash
zip [-r|--recurse-paths] path/to/archive.zip path/to/directory | tqdm --total $(find path/to/directory | wc [-l|--lines]) --unit files --null
```

### Create an archive with tar and create a progress bar (system agnostic, GNU tar uses `stdout` while BSD tar uses `stderr`)

```bash
tar vzcf path/to/archive.tar.gz path/to/directory 2>&1 | tqdm --total $(find path/to/directory | wc [-l|--lines]) --unit files --null
```

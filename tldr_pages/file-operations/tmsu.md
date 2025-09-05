# tmsu

> Simple tool for tagging files. More information: <https://tmsu.org>.

## Examples

### Tag a specific file with multiple tags

```bash
tmsu tag path/to/file.mp3 music big-jazz mp3
```

### Tag multiple files

```bash
tmsu tag --tags "music mp3" *.mp3
```

### List tags of specified file(s)

```bash
tmsu tags *.mp3
```

### List files with specified tag(s)

```bash
tmsu files big-jazz music
```

### List files with tags matching boolean expression

```bash
tmsu files "(year >= 1990 and year <= 2000) and grunge"
```

### Mount tmsu virtual filesystem to an existing directory

```bash
tmsu mount path/to/directory
```

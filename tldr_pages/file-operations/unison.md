# unison

> Bidirectional file synchronisation tool. More information: <https://github.com/bcpierce00/unison>.

## Examples

### Sync two directories (creates log first time these two directories are synchronized)

```bash
unison path/to/directory_1 path/to/directory_2
```

### Automatically accept the (non-conflicting) defaults

```bash
unison path/to/directory_1 path/to/directory_2 -auto
```

### Ignore some files using a pattern

```bash
unison path/to/directory_1 path/to/directory_2 -ignore pattern
```

### View documentation

```bash
unison -doc topics
```

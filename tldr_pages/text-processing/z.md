# z

> Tracks the most used (by frequency) directories and enables quickly navigating to them using string patterns or `regex`. More information: <https://github.com/rupa/z>.

## Examples

### Go to a directory that contains "foo" in the name

```bash
z foo
```

### Go to a directory that contains "foo" and then "bar"

```bash
z foo bar
```

### Go to the highest-ranked directory matching "foo"

```bash
z -r foo
```

### Go to the most recently accessed directory matching "foo"

```bash
z -t foo
```

### List all directories in `z`'s database matching "foo"

```bash
z -l foo
```

### Remove the current directory from `z`'s database

```bash
z -x
```

### Restrict matches to subdirectories of the current directory

```bash
z -c foo
```

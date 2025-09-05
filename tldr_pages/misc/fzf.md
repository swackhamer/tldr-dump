# fzf

> Fuzzy finder. Similar to `sk`. More information: <https://github.com/junegunn/fzf#usage>.

## Examples

### Start `fzf` on all files in the specified directory

```bash
find path/to/directory -type f | fzf
```

### Start `fzf` for running processes

```bash
ps aux | fzf
```

### Select multiple files with `<Shift Tab>` and write to a file

```bash
find path/to/directory -type f | fzf [-m|--multi] > path/to/file
```

### Start `fzf` with a specified query

```bash
fzf [-q|--query] "query"
```

### Start `fzf` on entries that start with `core` and end with either `go`, `rb`, or `py`

```bash
fzf [-q|--query] "^core go$ | rb$ | py$"
```

### Start `fzf` on entries that not match `pyc` and match exactly `travis`

```bash
fzf [-q|--query] "\!pyc 'travis'"
```

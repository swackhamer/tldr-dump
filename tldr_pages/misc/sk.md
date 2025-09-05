# sk

> Fuzzy finder written in Rust. Similar to `fzf`. More information: <https://github.com/lotabout/skim>.

## Examples

### Start `skim` on all files in the specified directory

```bash
find path/to/directory -type f | sk
```

### Start `skim` for running processes

```bash
ps aux | sk
```

### Start `skim` with a specified query

```bash
sk --query "query"
```

### Select multiple files with `<Shift Tab>` and write to a file

```bash
find path/to/directory -type f | sk --multi > path/to/file
```

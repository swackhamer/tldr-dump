# rip

> Remove files or directories by sending them to the graveyard, allowing for them to be recovered. More information: <https://github.com/nivekuil/rip>.

## Examples

### Remove files or directories from specified locations and place them in the graveyard

```bash
rip path/to/file_or_directory path/to/another/file_or_directory
```

### Interactively remove files or directories, with a prompt before every removal

```bash
rip --inspect path/to/file_or_directory path/to/another/file_or_directory
```

### List all files and directories in the graveyard that were originally within the current directory

```bash
rip --seance
```

### Permanently delete every file and directory in the graveyard

```bash
rip --decompose
```

### Put back the files and directories which were affected by the most recent removal

```bash
rip --unbury
```

### Put back every file and directory that is listed by `rip --seance`

```bash
rip --seance --unbury
```

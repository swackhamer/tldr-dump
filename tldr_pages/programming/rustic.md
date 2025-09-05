# rustic

> Create fast, encrypted, deduplicated backups powered by Rust. More information: <https://github.com/rustic-rs/rustic>.

## Examples

### Initialize a new repository

```bash
rustic init --repository /srv/rustic-repo
```

### Create a new backup of a file/directory to a repository

```bash
rustic backup --repository /srv/rustic-repo path/to/file_or_directory
```

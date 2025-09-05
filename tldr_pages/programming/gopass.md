# gopass

> Standard Unix Password Manager for Teams. Written in Go. More information: <https://www.gopass.pw>.

## Examples

### Initialize the configuration settings

```bash
gopass init
```

### Create a new entry

```bash
gopass new
```

### Show all stores

```bash
gopass mounts
```

### Mount a shared Git store

```bash
gopass mounts add store_name git_repo_url
```

### Search interactively using a keyword

```bash
gopass show keyword
```

### Search using a keyword

```bash
gopass find keyword
```

### Sync all mounted stores

```bash
gopass sync
```

### Show a particular password entry

```bash
gopass store_name|path/to/directory|email@email.com
```

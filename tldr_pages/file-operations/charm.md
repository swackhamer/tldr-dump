# charm

> Set of tools that makes adding a backend to your terminal-based applications, without worrying about user accounts, data storage and encryption. More information: <https://github.com/charmbracelet/charm>.

## Examples

### Backup your Charm account keys

```bash
charm backup-keys
```

### Backup Charm account keys to a specific location

```bash
charm backup-keys [-o|--output] path/to/output_file.tar
```

### Import previously backed up Charm account keys

```bash
charm import-keys "charm-keys-backup.tar"
```

### Find where your `cloud.charm.sh` folder resides on your machine

```bash
charm where
```

### Start your Charm server

```bash
charm serve
```

### Print linked SSH keys

```bash
charm keys
```

### Print your Charm ID

```bash
charm id
```

# ludusavi

> Backup video game save data. More information: <https://github.com/mtkennerly/ludusavi/blob/master/docs/cli.md>.

## Examples

### Backup games

```bash
ludusavi backup --path path/to/backup
```

### Restore games

```bash
ludusavi restore --path path/to/backup "game1" "game2" ...
```

### List backups

```bash
ludusavi backups --path path/to/backup
```

### Wrap launcher game

```bash
ludusavi wrap --gui --infer heroic|lutris|steam -- game_launch_commands
```

### Wrap standalone game

```bash
ludusavi wrap --gui --name name -- game_launch_commands
```

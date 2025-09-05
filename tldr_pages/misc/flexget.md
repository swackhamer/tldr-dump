# flexget

> A multipurpose automation tool for content like torrents, nzbs, podcasts, comics, series, movies, etc. More information: <https://flexget.com/en/CLI>.

## Examples

### Run all Flexget tasks now

```bash
flexget execute --now
```

### Start the Flexget daemon and daemonize its process

```bash
flexget daemon start --daemonize
```

### List all series recorded in Flexget

```bash
flexget series list
```

### Run a task from a configuration file

```bash
flexget -c path/to/config.yml execute --task task_name
```

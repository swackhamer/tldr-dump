# git-instaweb

> Helper to launch a GitWeb server. More information: <https://git-scm.com/docs/git-instaweb>.

## Examples

### Launch a GitWeb server for the current Git repository

```bash
git instaweb --start
```

### Listen only on localhost

```bash
git instaweb --start [-l|--local]
```

### Listen on a specific port

```bash
git instaweb --start [-p|--port] 1234
```

### Use a specified HTTP daemon

```bash
git instaweb --start [-d|--httpd] lighttpd|apache2|mongoose|plackup|webrick
```

### Also auto-launch a web browser

```bash
git instaweb --start [-b|--browser]
```

### Stop the currently running GitWeb server

```bash
git instaweb --stop
```

### Restart the currently running GitWeb server

```bash
git instaweb --restart
```

# mutagen

> Real-time file synchronization and network forwarding tool. More information: <https://mutagen.io/documentation/introduction/>.

## Examples

### Start a synchronization session between a local directory and a remote host

```bash
mutagen sync create --name=session_name /path/to/local/directory/ user@host:/path/to/remote/directory/
```

### Start a synchronization session between a local directory and a Docker container

```bash
mutagen sync create --name=session_name /path/to/local/directory/ docker://user@container_name/path/to/remote/directory/
```

### Stop a running session

```bash
mutagen sync terminate session_name
```

### Start a project

```bash
mutagen project start
```

### Stop a project

```bash
mutagen project terminate
```

### List running sessions for the current project

```bash
mutagen project list
```

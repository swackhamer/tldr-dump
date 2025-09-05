# openttd

> Open source clone of the Microprose game "Transport Tycoon Deluxe". More information: <https://wiki.openttd.org/en/Manual/Command%20line>.

## Examples

### Start a new game

```bash
openttd -g
```

### Load save game at start

```bash
openttd -g path/to/file
```

### Start with the specified window resolution

```bash
openttd -r 1920x1080
```

### Start with a custom configuration file

```bash
openttd -c path/to/file
```

### Start with selected video, sound, and music drivers

```bash
openttd -v video_driver -s sound_driver -m music_driver
```

### Start a dedicated server, forked in the background

```bash
openttd -f -D host:port
```

### Join a server with a password

```bash
openttd -n host:port#player_name -p password
```

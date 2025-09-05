# spotify_player

> A TUI Spotify client that implements all features of the official Spotify app. More information: <https://github.com/aome510/spotify-player#commands>.

## Examples

### Start a daemon that plays music in the background

```bash
spotify_player [-d|--daemon]
```

### Start the TUI (controls the daemon if available, otherwise starts its own client)

```bash
spotify_player
```

### Use the specified theme

```bash
spotify_player [-t|--theme] theme_name
```

### Use configuration files (`app.toml`, `keymap.toml` and `theme.toml`) in the specified directory

```bash
spotify_player [-c|--config-folder] path/to/directory
```

### Like the currently playing track

```bash
spotify_player like
```

### Display a list of keybindings

```bash
<?>
```

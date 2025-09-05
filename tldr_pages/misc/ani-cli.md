# ani-cli

> A cli to browse and watch anime. More information: <https://manned.org/ani-cli>.

## Examples

### Search anime by name

```bash
ani-cli "anime_name"
```

### Download an episode

```bash
ani-cli [-d|--download] "anime_name"
```

### Download a range of episodes

```bash
ani-cli [-d|--download] [-r|--range] "1 6" "anime_name"
```

### Download the entire series (a range of all episodes)

```bash
ani-cli [-d|--download] [-r|--range] "1 -1" "anime_name"
```

### Use VLC as the media player

```bash
ani-cli [-v|-vlc] "anime_name"
```

### Watch a specific episode

```bash
ani-cli [-e|--episode] episode_number "anime_name"
```

### Continue watching anime from history

```bash
ani-cli [-c|--continue]
```

### Update `ani-cli`

```bash
ani-cli [-U|--update]
```

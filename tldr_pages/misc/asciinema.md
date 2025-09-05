# asciinema

> Record and replay terminal sessions, and optionally share them on <https://asciinema.org>. See also: `terminalizer`. More information: <https://docs.asciinema.org/manual/cli/usage>.

## Examples

### Associate the local install of `asciinema` with an asciinema.org account

```bash
asciinema auth
```

### Make a new recording and save it to a local file (finish it with `<Ctrl d>` or type `exit`)

```bash
asciinema rec path/to/recording.cast
```

### Replay a terminal recording from a local file

```bash
asciinema play path/to/recording.cast
```

### Replay a terminal recording hosted on <https://asciinema.org>

```bash
asciinema play https://asciinema.org/a/cast_id
```

### Make a new recording, limiting any idle time to at most 2.5 seconds

```bash
asciinema rec [-i|--idle-time-limit] 2.5
```

### Print the full output of a locally saved recording

```bash
asciinema cat path/to/recording.cast
```

### Upload a locally saved terminal session to asciinema.org

```bash
asciinema upload path/to/recording.cast
```

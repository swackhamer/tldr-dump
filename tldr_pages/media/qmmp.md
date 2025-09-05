# qmmp

> An audio player with an interface similar to Winamp or XMMS. See also: `clementine`, `ncmpcpp`, `cmus`. More information: <https://manned.org/qmmp>.

## Examples

### Launch the GUI

```bash
qmmp
```

### Start or stop the currently playing audio

```bash
qmmp [-t|--play-pause]
```

### Seek [f]or[w]ar[d]s or [b]ack[w]ar[d]s a specific amount of time in seconds

```bash
qmmp --seek-fwd|bwd time_in_seconds
```

### Play the next audio file

```bash
qmmp --next
```

### Play the previous audio file

```bash
qmmp --previous
```

### Display the current volume

```bash
qmmp --volume-status
```

### [inc]rease or [dec]rease the volume of the currently playing audio by 5%

```bash
qmmp --volume-inc|dec
```

# mumble

> Low-latency, high quality voice chat software. More information: <https://www.mumble.info>.

## Examples

### Open Mumble

```bash
mumble
```

### Open Mumble and immediately connect to a server

```bash
mumble mumble://username@example.com
```

### Open Mumble and immediately connect to a password protected server

```bash
mumble mumble://username:password@example.com
```

### Mute/unmute the microphone in a running Mumble instance

```bash
mumble rpc mute|unmute
```

### Mute/unmute the microphone and the audio output of Mumble

```bash
mumble rpc deaf|undeaf
```

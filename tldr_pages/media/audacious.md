# audacious

> An open-source audio player. Indirectly based on XMMS. See also: `audtool`, `clementine`, `mpc`, `ncmpcpp`. More information: <https://audacious-media-player.org>.

## Examples

### Launch the GUI

```bash
audacious
```

### Start a new instance and play an audio

```bash
audacious --new-instance path/to/audio
```

### Enqueue a specific directory of audio files

```bash
audacious --enqueue path/to/directory
```

### Start or stop playback

```bash
audacious --play-pause
```

### Skip forwards ([fwd]) or backwards ([rew]) in the playlist

```bash
audacious --fwd|rew
```

### Stop playback

```bash
audacious --stop
```

### Start in CLI mode (headless)

```bash
audacious --headless
```

### Exit as soon as playback stops or there is nothing to playback

```bash
audacious --quit-after-play
```

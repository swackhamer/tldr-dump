# timidity

> Play and convert MIDI files. More information: <https://timidity.sourceforge.net>.

## Examples

### Play a MIDI file

```bash
timidity path/to/file.mid
```

### Play a MIDI file in a loop

```bash
timidity --loop path/to/file.mid
```

### Play a MIDI file in a specific key (0 = C major/A minor, -1 = F major/D minor, +1 = G major/E minor, etc.)

```bash
timidity --force-keysig=-flats|+sharps path/to/file.mid
```

### Convert a MIDI file to PCM (WAV) audio

```bash
timidity --output-mode=w --output-file=path/to/file.wav path/to/file.mid
```

### Convert a MIDI file to FLAC audio

```bash
timidity --output-mode=F --output-file=path/to/file.flac path/to/file.mid
```

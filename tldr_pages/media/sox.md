# sox

> Sound eXchange: play, record and convert audio files. Audio formats are identified by the extension. More information: <https://manned.org/sox>.

## Examples

### Merge two audio files into one

```bash
sox [-m|--combine mix] path/to/input_audio1 path/to/input_audio2 path/to/output_audio
```

### Trim an audio file to the specified times

```bash
sox path/to/input_audio path/to/output_audio trim start duration
```

### Normalize an audio file (adjust volume to the maximum peak level, without clipping)

```bash
sox --norm path/to/input_audio path/to/output_audio
```

### Reverse and save an audio file

```bash
sox path/to/input_audio path/to/output_audio reverse
```

### Print statistical data of an audio file

```bash
sox path/to/input_audio [-n|--null] stat
```

### Increase the volume of an audio file by 2x

```bash
sox [-v|--volume] 2.0 path/to/input_audio path/to/output_audio
```

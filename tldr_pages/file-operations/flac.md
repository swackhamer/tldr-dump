# flac

> Encodes, decodes and tests FLAC files. More information: <https://xiph.org/flac>.

## Examples

### Encode a WAV file to FLAC (this will create a FLAC file in the same location as the WAV file)

```bash
flac path/to/file.wav
```

### Encode a WAV file to FLAC, specifying the output file

```bash
flac [-o|--output-name] path/to/output.flac path/to/file.wav
```

### Decode a FLAC file to WAV, specifying the output file

```bash
flac [-d|--decode] [-o|--output-name] path/to/output.wav path/to/file.flac
```

### Test a FLAC file for the correct encoding

```bash
flac [-t|--test] path/to/file.flac
```

# lame

> Encode WAV to MP3 files. More information: <https://svn.code.sf.net/p/lame/svn/trunk/lame/USAGE>.

## Examples

### Encode an audio file to MP3 using CBR 320 kbit/second

```bash
lame -b 320 path/to/file.wav path/to/output.mp3
```

### Encode an audio file to MP3 using the V0 preset

```bash
lame -V 0 path/to/file.wav path/to/output.mp3
```

### Encode an audio file to AAC

```bash
lame path/to/file.wav path/to/output.aac
```

# musescore

> MuseScore 3 sheet music editor. See also: `lilypond`. More information: <https://musescore.org/en/handbook/4/command-line-options>.

## Examples

### Use a specific audio driver

```bash
musescore --audio-driver jack|alsa|portaudio|pulse
```

### Set the MP3 output bitrate in kbit/s

```bash
musescore --bitrate bitrate
```

### Start MuseScore in debug mode

```bash
musescore --debug
```

### Enable experimental features, such as layers

```bash
musescore --experimental
```

### Export the given file to the specified output file. The file type depends on the given extension

```bash
musescore --export-to output_file input_file
```

### Print a diff between the given scores

```bash
musescore --diff path/to/file1 path/to/file2
```

### Specify a MIDI import operations file

```bash
musescore --midi-operations path/to/file
```

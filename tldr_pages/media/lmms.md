# lmms

> Free, open source, cross-platform digital audio workstation. Render a `.mmp` or `.mmpz` project file, dump a `.mmpz` as XML, or start the GUI. See also: `mixxx`. More information: <https://lmms.io>.

## Examples

### Start the GUI

```bash
lmms
```

### Start the GUI and load external config

```bash
lmms --config path/to/config.xml
```

### Start the GUI and import MIDI or Hydrogen file

```bash
lmms --import path/to/midi/or/hydrogen/file
```

### Start the GUI with a specified window size

```bash
lmms --geometry x_sizexy_size+x_offset+y_offset
```

### Dump a `.mmpz` file

```bash
lmms dump path/to/mmpz/file.mmpz
```

### Render a project file

```bash
lmms render path/to/mmpz_or_mmp/file
```

### Render the individual tracks of a project file

```bash
lmms rendertracks path/to/mmpz_or_mmp/file path/to/dump/directory
```

### Render with custom samplerate, format, and as a loop

```bash
lmms render --samplerate 88200 --format ogg --loop --output path/to/output/file.ogg
```

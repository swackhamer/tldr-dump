# lilypond

> Typeset music and/or produce MIDI from file. See also: `musescore`. More information: <https://lilypond.org>.

## Examples

### Compile a lilypond file into a PDF

```bash
lilypond path/to/file
```

### Compile into the specified format

```bash
lilypond [-f|--format] format_dump path/to/file
```

### Compile the specified file, suppressing progress updates

```bash
lilypond [-s|--silent] path/to/file
```

### Compile the specified file, and also specify the output filename

```bash
lilypond [-o|--output] path/to/output_file path/to/input_file
```

### Show the current version of lilypond

```bash
lilypond [-v|--version]
```

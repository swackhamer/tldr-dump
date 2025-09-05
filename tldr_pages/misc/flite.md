# flite

> Speech synthesis engine. More information: <http://www.festvox.org/flite/doc/>.

## Examples

### List all available voices

```bash
flite -lv
```

### Convert a text string to speech

```bash
flite -t "string"
```

### Convert the contents of a file to speech

```bash
flite -f path/to/file.txt
```

### Use the specified voice

```bash
flite -voice file://path/to/filename.flitevox|url
```

### Store output into a wav file

```bash
flite -voice file://path/to/filename.flitevox|url -f path/to/file.txt -o output.wav
```

### Display version

```bash
flite --version
```

# vhs

> Generate terminal GIFs from a tape file. More information: <https://github.com/charmbracelet/vhs>.

## Examples

### Create a tape file (add commands to the tape file using an editor)

```bash
vhs new path/to/file.tape
```

### Record inputs to a tape file

```bash
vhs record > path/to/file.tape
```

### Record inputs to a tape file using a specific shell

```bash
vhs record [-s|--shell] shell > path/to/file.tape
```

### Stop recording

```bash
exit
```

### Validate the syntax of a tape file

```bash
vhs validate path/to/file.tape
```

### Create a GIF from a tape file

```bash
vhs path/to/file.tape
```

### Publish a GIF to <https://vhs.charm.sh> and get a shareable URL

```bash
vhs publish path/to/file.gif
```

# daps

> An open source program for transforming DocBook XML into output formats such as HTML or PDF. More information: <https://opensuse.github.io/daps/doc/index.html>.

## Examples

### Check if a DocBook XML file is valid

```bash
daps [-d|--docconfig] path/to/file.xml validate
```

### Convert a DocBook XML file into PDF

```bash
daps [-d|--docconfig] path/to/file.xml pdf
```

### Convert a DocBook XML file into a single HTML file

```bash
daps [-d|--docconfig] path/to/file.xml html --single
```

### Display help

```bash
daps [-h|--help]
```

### Display version

```bash
daps --version
```

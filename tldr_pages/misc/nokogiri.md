# nokogiri

> An HTML, XML, SAX and Reader parser. More information: <https://manned.org/nokogiri>.

## Examples

### Parse the contents of a URL or file

```bash
nokogiri url|path/to/file
```

### Parse as a specific type

```bash
nokogiri url|path/to/file --type xml|html
```

### Load a specific initialization file before parsing

```bash
nokogiri url|path/to/file -C path/to/config_file
```

### Parse using a specific encoding

```bash
nokogiri url|path/to/file [-E|--encoding] encoding
```

### Validate using a RELAX NG file

```bash
nokogiri url|path/to/file --rng url|path/to/file
```

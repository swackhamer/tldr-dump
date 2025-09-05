# xml

> XMLStarlet Toolkit: query, edit, check, convert and transform XML documents. Some subcommands such as `xml validate` have their own usage documentation. More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139670224>.

## Examples

### Display general help, including the list of subcommands

```bash
xml --help
```

### Execute a subcommand with input from a file or URI, printing to `stdout`

```bash
xml subcommand options path/to/input.xml|URI
```

### Execute a subcommand using `stdin` and `stdout`

```bash
xml subcommand options
```

### Execute a subcommand with input from a file or URI and output to a file

```bash
xml subcommand options path/to/input.xml|URI > path/to/output
```

### Display help for a specific subcommand

```bash
xml subcommand --help
```

### Display version

```bash
xml --version
```

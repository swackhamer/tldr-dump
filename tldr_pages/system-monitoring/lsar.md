# lsar

> List an archive file's contents. See also: `unar`, `ar`. More information: <https://manned.org/lsar>.

## Examples

### List an archive file's contents

```bash
lsar path/to/archive
```

### List a password protected archive file's contents

```bash
lsar path/to/archive [-p|--password] password
```

### Print all available information about each file in the archive (it's very long)

```bash
lsar [-L|--verylong] path/to/archive
```

### Test the integrity of the files in the archive (if possible)

```bash
lsar [-t|--test] path/to/archive
```

### List the archive file's contents in JSON format

```bash
lsar [-j|--json] path/to/archive
```

### Display help

```bash
lsar [-h|--help]
```

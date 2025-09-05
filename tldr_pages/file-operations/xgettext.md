# xgettext

> Extract gettext strings from code files. More information: <https://www.gnu.org/software/gettext/manual/gettext.html#xgettext-Invocation>.

## Examples

### Scan file and output strings to `messages.po`

```bash
xgettext path/to/input_file
```

### Use a different output filename

```bash
xgettext [-o|--output] path/to/output_file path/to/input_file
```

### Append new strings to an existing file

```bash
xgettext [-j|--join-existing] [-o|--output] path/to/output_file path/to/input_file
```

### Don't add a header containing metadata to the output file

```bash
xgettext --omit-header path/to/input_file
```

### Display help

```bash
xgettext [-h|--help]
```

# vale

> Extensible style checker that supports multiple markup formats, such as Markdown and AsciiDoc. More information: <https://vale.sh>.

## Examples

### Check the style of a file

```bash
vale path/to/file
```

### Check the style of a file with a specified configuration

```bash
vale --config='path/to/.vale.ini' path/to/file
```

### Output the results in JSON format

```bash
vale --output=JSON path/to/file
```

### Check style issues at the specific severity and higher

```bash
vale --minAlertLevel=suggestion|warning|error path/to/file
```

### Check the style from `stdin`, specifying markup format

```bash
cat file.md | vale --ext=.md
```

### List the current configuration

```bash
vale ls-config
```

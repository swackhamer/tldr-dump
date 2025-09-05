# ajson

> Execute JSONPath on JSON objects. More information: <https://github.com/spyzhov/ajson>.

## Examples

### Read JSON from a file and execute a specified JSONPath expression

```bash
ajson '$..json[?(@.path)]' path/to/file.json
```

### Read JSON from `stdin` and execute a specified JSONPath expression

```bash
cat path/to/file.json | ajson '$..json[?(@.path)]'
```

### Read JSON from a URL and evaluate a specified JSONPath expression

```bash
ajson 'avg($..price)' 'https://example.com/api/'
```

### Read some simple JSON and calculate a value

```bash
echo '3' | ajson '2 * pi * $'
```

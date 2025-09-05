# recsel

> Print records from a recfile: a human-editable, plain text database. More information: <https://www.gnu.org/software/recutils/manual/recutils.html#Invoking-recsel>.

## Examples

### Extract name and version field

```bash
recsel [-p|--print] name,version data.rec
```

### Use "~" to match a string with a given `regex`

```bash
recsel [-e|--expression] "field_name ~ 'regex' data.rec"
```

### Use a predicate to match a name and a version

```bash
recsel [-e|--expression] "name ~ 'regex' && version ~ 'regex'" data.rec
```

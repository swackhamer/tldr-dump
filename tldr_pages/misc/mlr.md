# mlr

> Miller is like `awk`, `sed`, `cut`, `join`, and `sort` for name-indexed data such as CSV, TSV, and tabular JSON. More information: <https://johnkerl.org/miller/doc>.

## Examples

### Pretty-print a CSV file in a tabular format

```bash
mlr --icsv --opprint cat example.csv
```

### Receive JSON data and pretty print the output

```bash
echo '{"hello":"world"}' | mlr --ijson --opprint cat
```

### Sort alphabetically on a field

```bash
mlr --icsv --opprint sort -f field example.csv
```

### Sort in descending numerical order on a field

```bash
mlr --icsv --opprint sort -nr field example.csv
```

### Convert CSV to JSON, performing calculations and display those calculations

```bash
mlr --icsv --ojson put '$newField1 = $oldFieldA/$oldFieldB' example.csv
```

### Receive JSON and format the output as vertical JSON

```bash
echo '{"hello":"world", "foo":"bar"}' | mlr --ijson --ojson --jvstack cat
```

### Filter lines of a compressed CSV file treating numbers as [S]trings

```bash
mlr --prepipe 'gunzip' [-c|--csv] filter [-S|--infer-none] '$fieldName =~ "regex"' example.csv.gz
```

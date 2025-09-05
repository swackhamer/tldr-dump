# csvsort

> Sort CSV files. Included in csvkit. More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>.

## Examples

### Sort a CSV file by column 9

```bash
csvsort [-c|--columns] 9 data.csv
```

### Sort a CSV file by the "name" column in descending order

```bash
csvsort [-r|--reverse] [-c|--columns] name data.csv
```

### Sort a CSV file by column 2, then by column 4

```bash
csvsort [-c|--columns] 2,4 data.csv
```

### Sort a CSV file without inferring data types

```bash
csvsort [-I|--no-inference] [-c|--columns] columns data.csv
```

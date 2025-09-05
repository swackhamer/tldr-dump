# csvstat

> Print descriptive statistics for all columns in a CSV file. Included in csvkit. More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html>.

## Examples

### Show all stats for all columns

```bash
csvstat data.csv
```

### Show all stats for columns 2 and 4

```bash
csvstat [-c|--columns] 2,4 data.csv
```

### Show sums for all columns

```bash
csvstat --sum data.csv
```

### Show the max value length for column 3

```bash
csvstat [-c|--columns] 3 --len data.csv
```

### Show the number of unique values in the "name" column

```bash
csvstat [-c|--columns] name --unique data.csv
```

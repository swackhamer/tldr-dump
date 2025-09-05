# xsv

> A CSV toolkit written in Rust. More information: <https://github.com/BurntSushi/xsv>.

## Examples

### Inspect the headers of a file

```bash
xsv headers path/to/file.csv
```

### Count the number of entries

```bash
xsv count path/to/file.csv
```

### Get an overview of the shape of entries

```bash
xsv stats path/to/file.csv | xsv table
```

### Select a few columns

```bash
xsv select column1,column2 path/to/file.csv
```

### Show 10 random entries

```bash
xsv sample 10 path/to/file.csv
```

### Join a column from one file to another

```bash
xsv join --no-case column1 path/to/file1.csv column2 path/to/file2.csv | xsv table
```

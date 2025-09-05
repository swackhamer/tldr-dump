# sort

> Sort lines of text files. More information: <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>.

## Examples

### Sort a file in ascending order

```bash
sort path/to/file
```

### Sort a file in descending order

```bash
sort [-r|--reverse] path/to/file
```

### Sort a file in case-insensitive way

```bash
sort [-f|--ignore-case] path/to/file
```

### Sort a file using numeric rather than alphabetic order

```bash
sort [-n|--numeric-sort] path/to/file
```

### Sort `/etc/passwd` by the 3rd field of each line numerically, using ":" as a field separator

```bash
sort [-t|--field-separator] : [-k|--key] 3n /etc/passwd
```

### As above, but when items in the 3rd field are equal, sort by the 4th field by numbers with exponents

```bash
sort [-t|--field-separator] : [-k|--key] 3,3n [-k|--key] 4,4g /etc/passwd
```

### Sort a file preserving only unique lines

```bash
sort [-u|--unique] path/to/file
```

### Sort a file, printing the output to the specified output file (can be used to sort a file in-place)

```bash
sort [-o|--output] path/to/file path/to/file
```

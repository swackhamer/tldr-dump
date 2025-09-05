# st.2

> Print basic descriptive statistics from input numbers. More information: <https://github.com/nferraz/st>.

## Examples

### Print count, min, max, sum, mean, and standard deviation for numbers in a file

```bash
st path/to/file
```

### Print statistics from standard input

```bash
cat path/to/file | st
```

### Print only the sum of the numbers

```bash
st [-s|--sum] path/to/file
```

### Print only the mean of the numbers

```bash
st [-m|--mean] path/to/file
```

### Print only the standard deviation

```bash
st [-s|--sd] path/to/file
```

### Transpose output (keys in one column, values in another)

```bash
st [-t|--transpose] path/to/file
```

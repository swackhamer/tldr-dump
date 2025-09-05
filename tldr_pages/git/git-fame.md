# git-fame

> Pretty-print Git repository contributions. More information: <https://manned.org/git-fame>.

## Examples

### Calculate contributions for the current Git repository

```bash
git fame
```

### Exclude files/directories that match the specified `regex`

```bash
git fame --excl "regex"
```

### Calculate contributions made after the specified date

```bash
git fame --since "3 weeks ago|2021-05-13"
```

### Display contributions in the specified format

```bash
git fame --format pipe|yaml|json|csv|tsv
```

### Display contributions per file extension

```bash
git fame [-t|--bytype]
```

### Ignore whitespace changes

```bash
git fame [-w|--ignore-whitespace]
```

### Detect inter-file line moves and copies

```bash
git fame -C
```

### Detect intra-file line moves and copies

```bash
git fame -M
```

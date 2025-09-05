# ifs

> IFS (Internal Field Separator) is a special environment variable that defines the delimiter used for word splitting in Unix shells. The default value of IFS is a space, tab, and newline. The three characters serve as delimiters. More information: <https://www.gnu.org/software/bash/manual/bash.html#Word-Splitting>.

## Examples

### View the current IFS value

```bash
echo "$IFS"
```

### Change the IFS value

```bash
IFS=":"
```

### Reset IFS to default

```bash
IFS=$' \t\n'
```

### Temporarily change the IFS value in a subshell

```bash
(IFS=":"; echo "one:two:three")
```

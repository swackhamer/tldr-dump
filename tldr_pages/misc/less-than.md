# less-than

> Redirect data to `stdin`. More information: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>.

## Examples

### Redirect a file to `stdin` (achieves the same effect as `cat file.txt |`)

```bash
command < path/to/file.txt
```

### Create a here document and pass that into `stdin` (requires a multiline command)

```bash
command << EOF <Enter> multiline_text <Enter> EOF
```

### Create a here string and pass that into `stdin` (achieves the same effect as `echo string |`)

```bash
command <<< string
```

### Process data from a file and write the output to another file

```bash
command < path/to/file.txt > path/to/file2.txt
```

### Write a here document into a file

```bash
cat << EOF > path/to/file.txt <Enter> multiline_data <Enter> EOF
```

### Disregard leading tabs (good for scripts with indentation but does not work for spaces)

```bash
cat <<- EOF > path/to/file.txt <Enter> multiline_data <Enter> EOF
```

### Pass command output to a program as a file descriptor

```bash
diff <(command1) <(command2)
```

### Open a persistent file descriptor

```bash
exec 3<path/to/file
```

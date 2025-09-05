# chmod

> Change the access permissions of a file or directory. More information: <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>.

## Examples

### Give the [u]ser who owns a file the right to e[x]ecute it

```bash
chmod u+x path/to/file
```

### Give the [u]ser rights to [r]ead and [w]rite to a file/directory

```bash
chmod u+rw path/to/file_or_directory
```

### Remove e[x]ecutable rights from the [g]roup

```bash
chmod g-x path/to/file
```

### Give [a]ll users rights to [r]ead and e[x]ecute

```bash
chmod a+rx path/to/file
```

### Give [o]thers (not in the file owner's group) the same rights as the [g]roup

```bash
chmod o=g path/to/file
```

### Remove all rights from [o]thers

```bash
chmod o= path/to/file
```

### Change permissions recursively giving [g]roup and [o]thers the ability to [w]rite

```bash
chmod [-R|--recursive] g+w,o+w path/to/directory
```

### Recursively give [a]ll users [r]ead permissions to files and e[X]ecute permissions to sub-directories within a directory

```bash
chmod [-R|--recursive] a+rX path/to/directory
```

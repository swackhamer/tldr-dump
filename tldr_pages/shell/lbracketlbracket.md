# [[

> Check file types and compare values. Returns a status of 0 if the condition evaluates to true, 1 if it evaluates to false. More information: <https://gnu.org/software/bash/manual/bash.html#index-_005b_005b>.

## Examples

### Test if a given variable is equal/not equal to the specified string

```bash
[[ $variable ==|!= "string" ]]
```

### Test if a given string conforms the specified glob/`regex`

```bash
[[ $variable ==|=~ pattern ]]
```

### Test if a given variable is [eq]ual/[n]ot [e]qual/[g]reater [t]han/[l]ess [t]han/[g]reater than or [e]qual/[l]ess than or [e]qual to the specified number

```bash
[[ $variable -eq|ne|gt|lt|ge|le integer ]]
```

### Test if the specified variable has a [n]on-empty value

```bash
[[ -n $variable ]]
```

### Test if the specified variable has an empty value ([z]ero length)

```bash
[[ -z $variable ]]
```

### Test if the specified [f]ile exists

```bash
[[ -f path/to/file ]]
```

### Test if the specified [d]irectory exists

```bash
[[ -d path/to/directory ]]
```

### Test if the specified file or directory [e]xists

```bash
[[ -e path/to/file_or_directory ]]
```

# read

> Shell builtin for retrieving data from `stdin`. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-read>.

## Examples

### Store data that you type from the keyboard

```bash
read variable
```

### Store each of the next lines you enter as values of an array

```bash
read -a array
```

### Specify the number of maximum characters to be read

```bash
read -n character_count variable
```

### Assign multiple values to multiple variables

```bash
read _ variable1 _ variable2 <<< "The surname is Bond"
```

### Do not let backslash (\\) act as an escape character

```bash
read -r variable
```

### Display a prompt before the input

```bash
read -p "Enter your input here: " variable
```

### Do not echo typed characters (silent mode)

```bash
read -s variable
```

### Read `stdin` and perform an action on every line

```bash
while read line; do echo|ls|rm|... "$line"; done < /dev/stdin|path/to/file|...
```

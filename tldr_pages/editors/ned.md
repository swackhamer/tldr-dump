# ned

> Like `grep` but with powerful replace capabilities. Unlike `sed`, as it isn't restricted to line oriented editing. More information: <https://github.com/nevdelap/ned>.

## Examples

### Recursively search starting in the current directory, ignoring case

```bash
ned --ignore-case --recursive '^[dl]og' .
```

### Search always showing colored output

```bash
ned --colors '^[dl]og' .
```

### Search never showing colored output

```bash
ned --colors=never '^[dl]og' .
```

### Search ignoring certain files

```bash
ned --recursive --exclude '*.htm' '^[dl]og' .
```

### Simple replace

```bash
ned 'dog' --replace 'cat' .
```

### Replace using numbered group references

```bash
ned 'the ([a-z]+) dog and the ([a-z]+) dog' --replace 'the $2 dog and the $1 dog' .
```

### Replace changing case

```bash
ned '([a-z]+) dog' --case-replacements --replace '\U$1\E! dog' --stdout .
```

### Preview results of a find and replace without updating the target files

```bash
ned '^[sb]ad' --replace 'happy' --stdout .
```

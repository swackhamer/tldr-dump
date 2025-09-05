# dirs

> Display or manipulate the directory stack. The directory stack is a list of recently visited directories that can be manipulated with the `pushd` and `popd` commands. See also: `pushd`, `popd`. More information: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

## Examples

### Display the directory stack with a space between each entry

```bash
dirs
```

### Display the directory stack with one entry per line

```bash
dirs -p
```

### Display a numbered list of entries in the directory stack

```bash
dirs -v
```

### Display the directory stack without the tilde-prefix (`~`)

```bash
dirs -l
```

### Display only the `n`th entry in the directory stack, starting at 0 (Bash only)

```bash
dirs +n
```

### Display only the `n`th entry in the directory stack from the last, starting at 0 (Bash only)

```bash
dirs -n
```

### Clear the directory stack

```bash
dirs -c
```

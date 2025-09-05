# ^

> Bash builtin to quick substitute a string in the previous command and run the result. Equivalent to `!!:s^string1^string2`. More information: <https://gnu.org/software/bash/manual/bash.html#Event-Designators>.

## Examples

### Run the previous command replacing `string1` with `string2`

```bash
^string1^string2
```

### Remove `string1` from the previous command

```bash
^string1^
```

### Replace `string1` with `string2` in the previous command and add `string3` to its end

```bash
^string1^string2^string3
```

### Replace all occurrences of `string1`

```bash
^string1^string2^:g&
```

### Print the substituted command without running it

```bash
^string1^string2^:p
```

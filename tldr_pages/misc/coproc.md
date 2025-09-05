# coproc

> Bash builtin for creating interactive asynchronous subshells. More information: <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

## Examples

### Run a subshell asynchronously

```bash
coproc { command1; command2; ...; }
```

### Create a coprocess with a specific name

```bash
coproc name { command1; command2; ...; }
```

### Write to a specific coprocess `stdin`

```bash
echo "input" >&"${name[1]}"
```

### Read from a specific coprocess `stdout`

```bash
read variable <&"${name[0]}"
```

### Create a coprocess which repeatedly reads `stdin` and runs some commands on the input

```bash
coproc name { while read line; do command1; command2; ...; done }
```

### Create a coprocess which repeatedly reads `stdin`, runs a pipeline on the input, and writes the output to `stdout`

```bash
coproc name { while read line; do echo "$line" | command1 | command2 | ... | cat /dev/fd/0; done }
```

### Create and use a coprocess running `bc`

```bash
coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"
```

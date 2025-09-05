# bash

> Bourne-Again SHell, an `sh`-compatible command-line interpreter. See also: `zsh`, `histexpand` (history expansion). More information: <https://www.gnu.org/software/bash/manual/bash.html#Invoking-Bash>.

## Examples

### Start an interactive shell session

```bash
bash
```

### Start an interactive shell session without loading startup configs

```bash
bash --norc
```

### Execute specific [c]ommands

```bash
bash -c "echo 'bash is executed'"
```

### Execute a specific script

```bash
bash path/to/script.sh
```

### E[x]ecute a specific script, printing each command before executing it

```bash
bash -x path/to/script.sh
```

### Execute a specific script and stop at the first [e]rror

```bash
bash -e path/to/script.sh
```

### Execute specific commands from `stdin`

```bash
echo "echo 'bash is executed'" | bash
```

### Start a [r]estricted shell session

```bash
bash -r
```

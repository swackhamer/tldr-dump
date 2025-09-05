# yes

> Output something repeatedly. This command is commonly used to answer yes to every prompt by install commands (such as apt-get). More information: <https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

## Examples

### Repeatedly output "message"

```bash
yes message
```

### Repeatedly output "y"

```bash
yes
```

### Accept everything prompted by the `apt-get` command

```bash
yes | sudo apt-get install program
```

### Repeatedly output a newline to always accept the default option of a prompt

```bash
yes ''
```

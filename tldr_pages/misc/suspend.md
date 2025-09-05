# suspend

> Suspend the execution of the current shell. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-suspend>.

## Examples

### Suspend the current shell (useful for when you are in nested shells like `su`)

```bash
bash <Enter> suspend
```

### Continue from suspension if `suspend` was used in a non-nested shell (run this in a separate terminal)

```bash
pkill -CONT bash
```

### Force suspension even if this would lock you out of the system

```bash
suspend -f
```

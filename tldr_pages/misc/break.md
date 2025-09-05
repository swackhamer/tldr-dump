# break

> Break out of a `for`, `while`, `until` or `select` loop. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-break>.

## Examples

### Break out of a single loop

```bash
while :; do break; done
```

### Break out of nested loops

```bash
while :; do while :; do break 2; done; done
```

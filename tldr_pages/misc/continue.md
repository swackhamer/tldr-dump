# continue

> Skip to the next iteration of a `for`, `while`, `until` or `select` loop. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-continue>.

## Examples

### Skip to the next iteration

```bash
while :; do continue; echo "This will never be reached"; done
```

### Skip to the next iteration from within a nested loop

```bash
for i in {1..3}; do echo $i; while :; do continue 2; done; done
```

# nproc

> Print the number of processing units (normally CPUs) available. More information: <https://www.gnu.org/software/coreutils/manual/html_node/nproc-invocation.html>.

## Examples

### Display the number of available processing units

```bash
nproc
```

### Display the number of installed processing units, including any inactive ones

```bash
nproc --all
```

### If possible, subtract a given number of units from the returned value

```bash
nproc --ignore count
```

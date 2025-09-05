# numfmt

> Convert numbers to and from human-readable strings. More information: <https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>.

## Examples

### Convert 1.5K (SI Units) to 1500

```bash
numfmt --from si 1.5K
```

### Convert 5th field (1-indexed) to IEC Units without converting header

```bash
ls -l | numfmt --header=1 --field 5 --to iec
```

### Convert to IEC units, pad with 5 characters, left aligned

```bash
du [-s|--summarize] * | numfmt --to iec --format "%-5f"
```

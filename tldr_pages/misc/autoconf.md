# autoconf

> Generate configuration scripts to automatically configure software source code packages. More information: <https://manned.org/autoconf>.

## Examples

### Generate a configuration script from `configure.ac` (if present) or `configure.in` and save this script to `configure`

```bash
autoconf
```

### Generate a configuration script from the specified template; output to `stdout`

```bash
autoconf template-file
```

### Generate a configuration script from the specified template (even if the input file has not changed) and write the output to a file

```bash
autoconf [-f|--force] [-o|--output] outfile template-file
```

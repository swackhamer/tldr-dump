# pamoil

> Turn a PAM image into an oil painting. More information: <https://netpbm.sourceforge.net/doc/pamoil.html>.

## Examples

### Turn a PAM image into an oil painting

```bash
pamoil path/to/input_file.pam > path/to/output_file.pam
```

### Consider a neighborhood of `n` pixels for the "smearing" effect

```bash
pamoil -n n path/to/input_file.pam > path/to/output_file.pam
```

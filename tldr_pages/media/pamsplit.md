# pamsplit

> Split a multi-image Netpbm file into multiple single-image Netpbm files. See also: `pamfile`, `pampick`, `pamexec`. More information: <https://netpbm.sourceforge.net/doc/pamsplit.html>.

## Examples

### Split a multi-image Netpbm file into multiple single-image Netpbm files

```bash
pamsplit path/to/image.pam
```

### Specify a pattern for naming output files

```bash
pamsplit path/to/image.pam file_%d.pam
```

# ipaggmanip

> Manipulate aggregate statistics produced by `ipaggcreate`. More information: <https://manned.org/ipaggmanip>.

## Examples

### Combine labels equal in their high-order bits

```bash
ipaggmanip [-p|--prefix] 16 path/to/file
```

### Remove labels with a count smaller than a given number of bytes and output a random sample of such labels

```bash
ipaggmanip --cut-smaller 100 --cull-labels 5 path/to/file
```

### Replace each label's count with 1 if it is non-zero

```bash
ipaggmanip [-P|--posterize] path/to/file
```

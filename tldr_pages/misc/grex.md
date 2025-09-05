# grex

> Generate `regex`s. More information: <https://github.com/pemistahl/grex>.

## Examples

### Generate a simple `regex`

```bash
grex space_separated_strings
```

### Generate a case-insensitive `regex`

```bash
grex [-i|--ignore-case] space_separated_strings
```

### Replace digits with '\d'

```bash
grex [-d|--digits] space_separated_strings
```

### Replace Unicode word character with '\w'

```bash
grex [-w|--words] space_separated_strings
```

### Replace spaces with '\s'

```bash
grex [-s|--spaces] space_separated_strings
```

### Add {min, max} quantifier representation for repeating sub-strings

```bash
grex [-r|--repetitions] space_separated_strings
```

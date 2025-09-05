# bb

> Native Clojure interpreter for scripting. More information: <https://book.babashka.org/#usage>.

## Examples

### Evaluate an expression

```bash
bb [-e|--eval] "(+ 1 2 3)"
```

### Evaluate a script file

```bash
bb [-f|--file] path/to/script.clj
```

### Bind [i]nput to a sequence of lines from `stdin`

```bash
printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"
```

### Bind [I]nput to a sequence of EDN (Extensible Data Notation) values from `stdin`

```bash
echo "{:key 'val}" | bb -I "(:key (first *input*))"
```

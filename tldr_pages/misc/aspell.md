# aspell

> Interactive spell checker. More information: <http://aspell.net/man-html/index.html>.

## Examples

### Spell check a single file

```bash
aspell check path/to/file
```

### List misspelled words from `stdin`

```bash
cat path/to/file | aspell list
```

### Show available dictionary languages

```bash
aspell dicts
```

### Run `aspell` with a different language (takes two-letter ISO 639 language code)

```bash
aspell --lang cs
```

### List misspelled words from `stdin` and ignore words from personal word list

```bash
cat path/to/file | aspell --personal personal-word-list.pws list
```

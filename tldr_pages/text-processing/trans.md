# trans

> Translate Shell, a command-line translator. More information: <https://github.com/soimort/translate-shell>.

## Examples

### Translate a word (language is detected automatically)

```bash
trans "word_or_sentence_to_translate"
```

### Get a brief translation

```bash
trans [-b|-brief] "word_or_sentence_to_translate"
```

### Translate a word into french

```bash
trans :fr word
```

### Translate a word from German to English

```bash
trans de:en Schmetterling
```

### Behave like a dictionary to get the meaning of a word

```bash
trans [-d|-dictionary] word
```

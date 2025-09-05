# argos-translate

> An open-source offline translation library and CLI tool written in Python. More information: <https://argos-translate.readthedocs.io/en/latest/source/cli.html>.

## Examples

### Install translation pairs for Spanish to English translation

```bash
argospm install translate-es_en
```

### Translate some text from Spanish (`es`) to English (`en`) (Note: Only two letter language codes are supported)

```bash
argos-translate --from-lang es --to-lang en un texto corto
```

### Translate a text file from English to Hindi

```bash
cat path/to/file.txt | argos-translate --from-lang en --to-lang hi
```

### List all installed translation pairs

```bash
argospm list
```

### Show translation pairs from English that are available to be installed

```bash
argospm search --from-lang en
```

### Update installed language package pairs

```bash
argospm update
```

### Translate from `ar` to `ru` (Note: This requires the translation pairs `translate-ar_en` and `translate-en_ru` to be installed)

```bash
argos-translate --from-lang ar --to-lang ru صورة تساوي أكثر من ألف كلمة
```

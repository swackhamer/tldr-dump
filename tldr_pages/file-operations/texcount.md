# texcount

> Count words in TeX documents omitting macros. Note: If the TeX document uses `\include` or `\input` and you want to count the included files, `texcount` must be run in the directory of the root TeX file. More information: <https://app.uio.no/ifi/texcount/howto.html>.

## Examples

### Count words in a TeX file

```bash
texcount path/to/file.tex
```

### Count words in a document and subdocuments built with `\input` or `\include`

```bash
texcount -merge file.tex
```

### Count words in a document and subdocuments, listing each file separately (and a total count)

```bash
texcount -inc file.tex
```

### Count words in a document and subdocuments, producing subcounts by chapter (instead of subsection)

```bash
texcount -merge -sub=chapter file.tex
```

### Count words with verbose output

```bash
texcount -v path/to/file.tex
```

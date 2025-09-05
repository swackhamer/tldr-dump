# codespell

> Spellchecker for source code. More information: <https://github.com/codespell-project/codespell>.

## Examples

### Check for typos in all text files in the current directory, recursively

```bash
codespell
```

### Correct all typos found in-place

```bash
codespell --write-changes
```

### Skip files with names that match the specified pattern (accepts a comma-separated list of patterns using wildcards)

```bash
codespell --skip "pattern"
```

### Use a custom dictionary file when checking (`--dictionary` can be used multiple times)

```bash
codespell --dictionary path/to/file.txt
```

### Do not check words that are listed in the specified file

```bash
codespell --ignore-words path/to/file.txt
```

### Do not check the specified words

```bash
codespell --ignore-words-list ignored_word1,ignored_word2,...
```

### Print 3 lines of context around, before or after each match

```bash
codespell --context|before-context|after-context 3
```

### Check file names for typos, in addition to file contents

```bash
codespell --check-filenames
```

# brew-search

> Search for casks and formulae. More information: <https://docs.brew.sh/Manpage#search--s-options-textregex->.

## Examples

### Search for casks and formulae using a keyword

```bash
brew search keyword
```

### Search for casks and formulae using a `regex`

```bash
brew search /regex/
```

### Enable searching through descriptions

```bash
brew search --desc keyword
```

### Only search for formulae

```bash
brew search --formula keyword
```

### Only search for casks

```bash
brew search --cask keyword
```

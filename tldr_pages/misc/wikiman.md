# wikiman

> Offline search engine for documentation. Supports manual pages, Arch Wiki, Gentoo Wiki, FreeBSD documentation, and tldr-pages. More information: <https://github.com/filiparag/wikiman>.

## Examples

### Search for a specific topic in all installed sources

```bash
wikiman search_term
```

### Search for a topic in a specific [s]ource

```bash
wikiman -s source search_term
```

### Search for a topic in two or more specific [s]ources

```bash
wikiman -s source1,source2,... search_term
```

### List existing [S]ources

```bash
wikiman -S
```

### Display [h]elp

```bash
wikiman -h
```

# surfraw

> Query a variety of web search engines. Consists of a collection of elvi, each of which knows how to search a website. More information: <https://manned.org/surfraw>.

## Examples

### Display the list of supported website search scripts (elvi)

```bash
surfraw -elvi
```

### Open the elvi's results page for a specific search in the browser

```bash
surfraw elvi_name "search_terms"
```

### Display an elvi description and its specific options

```bash
surfraw elvi_name [-lh|-local-help]
```

### Search using an elvi with specific options and open the results page in the browser

```bash
surfraw elvi_name elvi_options "search_terms"
```

### Display the URL to the elvi's results page for a specific search

```bash
surfraw -print elvi_name "search_terms"
```

### Search using the alias

```bash
sr elvi_name "search_terms"
```

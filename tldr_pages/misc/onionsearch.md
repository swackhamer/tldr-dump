# onionsearch

> Scrape URLs on different `.onion` search engines. Note: `onionsearch` requires a Tor proxy running on `localhost:9050`; a Tor enabled browser is needed to visit the `.onion` websites. More information: <https://github.com/megadose/OnionSearch>.

## Examples

### Request results from all the search engines

```bash
onionsearch "string"
```

### Request search results from specific search engines

```bash
onionsearch "string" --engines tor66 deeplink phobos ...
```

### Exclude certain search engines when searching

```bash
onionsearch "string" --exclude candle ahmia ...
```

### Limit the number of pages to load per engine

```bash
onionsearch "stuxnet" --engines tor66 deeplink phobos ... --limit 3
```

### List all supported search engines

```bash
onionsearch --help | grep [-A|--after-context] 1 [-i|--ignore-case] "supported engines"
```

# mas

> Command-line interface for the Mac App Store. More information: <https://github.com/mas-cli/mas>.

## Examples

### Sign into the Mac App Store for the first time

```bash
mas signin "user@example.com"
```

### Show all installed applications and their product identifiers

```bash
mas list
```

### Search for an application, displaying the price alongside the results

```bash
mas search "application" --price
```

### Install or update an application using exact numeric id

```bash
mas install numeric_product_id
```

### Install the first application that would be returned by the respective search

```bash
mas lucky "search_term"
```

### List all outdated apps with pending updates

```bash
mas outdated
```

### Install all pending updates

```bash
mas upgrade
```

### Upgrade a specific application

```bash
mas upgrade "numeric_product_id"
```

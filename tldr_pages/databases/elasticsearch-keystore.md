# elasticsearch-keystore

> Manage secure settings (e.g., passwords, tokens, and credentials) used by Elasticsearch. More information: <https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-keystore.html>.

## Examples

### Create a new keystore (not password-protected)

```bash
elasticsearch-keystore create
```

### Create a new password-protected keystore

```bash
elasticsearch-keystore create -p
```

### Add a setting interactively

```bash
elasticsearch-keystore add setting_name
```

### Add a setting from standard input

```bash
echo "setting_value" | elasticsearch-keystore add --stdin setting_name
```

### Remove a setting from the keystore

```bash
elasticsearch-keystore remove setting_name
```

### Change the keystore password

```bash
elasticsearch-keystore passwd
```

### List all settings stored in the keystore

```bash
elasticsearch-keystore list
```

### Upgrade the keystore format (after an Elasticsearch upgrade)

```bash
elasticsearch-keystore upgrade
```

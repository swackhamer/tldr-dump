# elasticsearch-create-enrollment-token

> Create enrollment tokens for Elasticsearch nodes and Kibana instances. More information: <https://www.elastic.co/guide/en/elasticsearch/reference/current/create-enrollment-token.html>.

## Examples

### Create an enrollment token for adding a new Elasticsearch node

```bash
elasticsearch-create-enrollment-token [-s|--scope] node
```

### Create an enrollment token for adding a new Kibana instance

```bash
elasticsearch-create-enrollment-token [-s|--scope] kibana
```

### Create an enrollment token and display verbose output

```bash
elasticsearch-create-enrollment-token [-s|--scope] node --verbose
```

### Create an enrollment token for a Kibana instance with a custom Elasticsearch URL

```bash
elasticsearch-create-enrollment-token [-s|--scope] kibana --url "IP"
```

### Display help

```bash
elasticsearch-create-enrollment-token [-h|--help]
```

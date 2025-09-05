# elasticsearch-node

> Manage low-level Elasticsearch node operations such as shutdown, repurpose, or viewing info. More information: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/node-tool>.

## Examples

### Display information about the current node

```bash
elasticsearch-node info
```

### Prepare the node for a full cluster restart (e.g., after upgrading)

```bash
elasticsearch-node unsafe-bootstrap
```

### Repurpose a node for a different role (e.g., from master to data node)

```bash
elasticsearch-node repurpose
```

### List the roles assigned to the node

```bash
elasticsearch-node roles
```

### Show the installed JVM version, Elasticsearch home path, and other diagnostic information

```bash
elasticsearch-node diagnostics
```

### Display help

```bash
elasticsearch-node [-h|--help]
```

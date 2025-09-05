# cypher-shell

> Open an interactive session and run Cypher queries against a Neo4j instance. See also: `neo4j-admin`, `mysql`. More information: <https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/>.

## Examples

### Connect to a local instance on the default port (`neo4j://localhost:7687`)

```bash
cypher-shell
```

### Connect to a remote instance

```bash
cypher-shell --address neo4j://host:port
```

### Connect and supply security credentials

```bash
cypher-shell --username username --password password
```

### Connect to a specific database

```bash
cypher-shell --database database_name
```

### Execute Cypher statements in a file and close

```bash
cypher-shell --file path/to/file.cypher
```

### Enable logging to a file

```bash
cypher-shell --log path/to/file.log
```

### Display help

```bash
cypher-shell --help
```

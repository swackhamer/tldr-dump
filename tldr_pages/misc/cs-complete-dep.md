# cs-complete-dep

> Search for libraries without doing it directly on the web. More information: <https://get-coursier.io/docs/cli-complete>.

## Examples

### Print which artifacts are published under a specific Maven group identifier

```bash
cs complete-dep group_id
```

### List published library versions under a specific Maven group identifier and an artifact one

```bash
cs complete-dep group_id:artifact_id
```

### Print which artifacts are pubblished under a given Maven groupId searching in the ivy2local

```bash
cs complete-dep group_id --repository ivy2local
```

### List published artifacts under a Maven group identifier searching in a specific repository and credentials

```bash
cs complete-dep group_id:artifact_id --repository repository_url --credentials user:password
```

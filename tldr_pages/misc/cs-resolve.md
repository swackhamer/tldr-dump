# cs-resolve

> Resolve lists the transitive dependencies of other dependencies. More information: <https://get-coursier.io/docs/cli-resolve>.

## Examples

### Resolve lists of transitive dependencies of two dependencies

```bash
cs resolve group_id1:artifact_id1:artifact_version1 group_id2:artifact_id2:artifact_version2
```

### Resolve lists of transitive dependencies of a package by the dependency tree

```bash
cs resolve --tree group_id:artifact_id:artifact_version
```

### Resolve dependency tree in a reverse order (from a dependency to its dependencies)

```bash
cs resolve --reverse-tree group_id:artifact_id:artifact_version
```

### Print all the libraries that depends on a specific library

```bash
cs resolve group_id:artifact_id:artifact_version --what-depends-on searched_group_id:searched_artifact_id
```

### Print all the libraries that depends on a specific library version

```bash
cs resolve group_id:artifact_id:artifact_version --what-depends-on searched_group_id:searched_artifact_idsearched_artifact_version
```

### Print eventual conflicts between a set of packages

```bash
cs resolve --conflicts group_id1:artifact_id1:artifact_version1 group_id2:artifact_id2:artifact_version2 ...
```

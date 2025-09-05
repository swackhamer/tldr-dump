# stolonctl

> CLI for Stolon, a cloud native PostgreSQL manager for PostgreSQL high availability. More information: <https://github.com/sorintlab/stolon>.

## Examples

### Get cluster status

```bash
stolonctl --cluster-name cluster_name --store-backend store_backend --store-endpoints store_endpoints status
```

### Get cluster data

```bash
stolonctl --cluster-name cluster_name --store-backend store_backend --store-endpoints store_endpoints clusterdata
```

### Get cluster specification

```bash
stolonctl --cluster-name cluster_name --store-backend store_backend --store-endpoints store_endpoints spec
```

### Update cluster specification with a patch in JSON format

```bash
stolonctl --cluster-name cluster_name --store-backend store_backend --store-endpoints store_endpoints update --patch 'cluster_spec'
```

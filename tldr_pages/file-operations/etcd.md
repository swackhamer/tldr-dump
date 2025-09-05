# etcd

> A distributed, reliable key-value store for the most critical data of a distributed system. More information: <https://etcd.io>.

## Examples

### Start a single-node etcd cluster

```bash
etcd
```

### Start a single-node etcd cluster, listening for client requests on a custom URL

```bash
etcd --advertise-client-urls http://127.0.0.1:1234 --listen-client-urls http://127.0.0.1:1234
```

### Start a single-node etcd cluster with a custom name

```bash
etcd --name my_etcd_cluster
```

### Start a single-node etcd cluster with extensive metrics available at <http://localhost:2379/debug/pprof/>

```bash
etcd --enable-pprof --metrics extensive
```

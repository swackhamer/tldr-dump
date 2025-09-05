# etcdctl

> Interact with `etcd`, a highly-available key-value pair store. More information: <https://etcd.io/docs/latest/dev-guide/interacting_v3/>.

## Examples

### Display the value associated with a specified key

```bash
etcdctl get my/key
```

### Store a key-value pair

```bash
etcdctl put my/key my_value
```

### Delete a key-value pair

```bash
etcdctl del my/key
```

### Store a key-value pair, reading the value from a file

```bash
etcdctl put my/file < path/to/file.txt
```

### Save a snapshot of the etcd keystore

```bash
etcdctl snapshot save path/to/snapshot.db
```

### Restore a snapshot of an etcd keystore (restart the etcd server afterwards)

```bash
etcdctl snapshot restore path/to/snapshot.db
```

### Add a user

```bash
etcdctl user add my_user
```

### Watch a key for changes

```bash
etcdctl watch my/key
```

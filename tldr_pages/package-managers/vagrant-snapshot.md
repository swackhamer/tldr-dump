# vagrant-snapshot

> Manage snapshots of Vagrant machines. See also: `vagrant`. More information: <https://developer.hashicorp.com/vagrant/docs/cli/snapshot>.

## Examples

### Take a snapshot of the machine (running or stopped)

```bash
vagrant snapshot save snapshot_name
```

### Restore a snapshot and start the machine

```bash
vagrant snapshot restore snapshot_name
```

### Restore a snapshot without starting the machine

```bash
vagrant snapshot restore --no-start snapshot_name
```

### Delete a snapshot

```bash
vagrant snapshot delete snapshot_name
```

### List available snapshots of the machine

```bash
vagrant snapshot list
```

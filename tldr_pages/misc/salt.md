# salt

> Execute commands and assert state on remote salt minions. More information: <https://docs.saltproject.io/en/latest/ref/cli/index.html>.

## Examples

### List connected minions

```bash
salt '*' test.ping
```

### Execute a highstate on all connected minions

```bash
salt '*' state.highstate
```

### Upgrade packages using the OS package manager (apt, yum, brew) on a subset of minions

```bash
salt '*.example.com' pkg.upgrade
```

### Execute an arbitrary command on a particular minion

```bash
salt 'minion_id' cmd.run "ls "
```

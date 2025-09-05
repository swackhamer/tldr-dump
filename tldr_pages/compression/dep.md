# dep

> Deploy PHP applications. Note: The Go command `dep` with the same name is deprecated and archived. More information: <https://deployer.org>.

## Examples

### Interactively initialize deployer in the local path (use a framework template with `--template=template`)

```bash
dep init
```

### Deploy an application to a remote host

```bash
dep deploy hostname
```

### Rollback to the previous working release

```bash
dep rollback
```

### Connect to a remote host via SSH

```bash
dep ssh hostname
```

### List commands

```bash
dep list
```

### Run any arbitrary command on the remote hosts

```bash
dep run "command"
```

### Display help for a command

```bash
dep help command
```

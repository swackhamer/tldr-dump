# nagios2

> Legacy host/service/networking monitoring program. Largely deprecated by `nagios4`. See also: `nagios`, `nagios3`, `nagios4`. More information: <https://manned.org/nagios>.

## Examples

### Start `nagios2`

```bash
nagios2 /etc/nagios2/nagios.cfg
```

### Start `nagios2` in daemon mode

```bash
nagios2 -d
```

### Start `nagios2`, print service check scheduling information to `stdout`, then shutdown

```bash
nagios2 -s
```

### Verify configuration file

```bash
nagios2 -v
```

# nagios3

> Legacy host/service/networking monitoring program. Largely deprecated by `nagios4`. See also: `nagios`, `nagios2`, `nagios4`. More information: <https://manned.org/nagios>.

## Examples

### Start `nagios3`

```bash
nagios3 /etc/nagios3/nagios.cfg
```

### Start `nagios3` in daemon mode

```bash
nagios3 -d
```

### Start `nagios3`, print service check scheduling information to `stdout`, then shutdown

```bash
nagios3 -s
```

### Verify configuration file

```bash
nagios3 -v
```

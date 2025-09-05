# nagios

> Legacy host/service/networking monitoring program. Largely deprecated by `nagios4`. See also: `nagios2`, `nagios3`, `nagios4`. More information: <https://manned.org/nagios>.

## Examples

### Start `nagios`

```bash
nagios /etc/nagios/nagios.cfg
```

### Start `nagios` in daemon mode

```bash
nagios -d
```

### Start `nagios`, print service check scheduling information to `stdout`, then shutdown

```bash
nagios -s
```

### Verify configuration file

```bash
nagios -v
```

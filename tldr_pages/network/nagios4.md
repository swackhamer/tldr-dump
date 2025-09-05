# nagios4

> Legacy host/service/networking monitoring program. See also: `nagios`, `nagios2`, `nagios3`. More information: <https://manned.org/nagios>.

## Examples

### Start `nagios4`

```bash
nagios4 /etc/nagios4/nagios.cfg
```

### Start `nagios4` in daemon mode

```bash
nagios4 -d
```

### Start `nagios4`, print service check scheduling information to `stdout`, then shutdown

```bash
nagios4 -s
```

### Verify configuration file

```bash
nagios4 -v
```

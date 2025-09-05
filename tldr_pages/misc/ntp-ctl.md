# ntp-ctl

> Management client for the `ntpd-rs` daemon. More information: <https://docs.ntpd-rs.pendulum-project.org/man/ntp-ctl.8>.

## Examples

### Display information about the current state of the NTP daemon

```bash
ntp-ctl status
```

### Check if the specified configuration file (default: `/etc/ntpd-rs/ntp.toml`) is valid

```bash
ntp-ctl [-c|--config] path/to/config validate
```

### Interactively run a single synchronization of the clock

```bash
sudo ntp-ctl force-sync
```

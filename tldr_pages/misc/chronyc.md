# chronyc

> Query the Chrony NTP daemon. More information: <https://chrony-project.org/doc/4.6.1/chronyc.html>.

## Examples

### Start `chronyc` in interactive mode

```bash
chronyc
```

### Display tracking stats for the Chrony daemon

```bash
chronyc tracking
```

### Print the time sources that Chrony is currently using

```bash
chronyc sources
```

### Display stats for sources currently used by chrony daemon as a time source

```bash
chronyc sourcestats
```

### Step the system clock immediately, bypassing any slewing

```bash
chronyc makestep
```

### Display verbose information about each NTP source

```bash
chronyc ntpdata
```

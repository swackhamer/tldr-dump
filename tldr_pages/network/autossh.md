# autossh

> Run, monitor and restart SSH connections. Auto-reconnects to keep port forwarding tunnels up. Accepts all SSH flags. More information: <https://manned.org/autossh>.

## Examples

### Start an SSH session, restarting when the [M]onitoring port fails to return data

```bash
autossh -M monitor_port "ssh_command"
```

### Forward a [L]ocal port to a remote one, restarting when necessary

```bash
autossh -M monitor_port -L local_port:localhost:remote_port user@host
```

### Fork `autossh` into the background before executing SSH and do [N]ot open a remote shell

```bash
autossh -f -M monitor_port -N "ssh_command"
```

### Run in the background, with no monitoring port, and instead send SSH keep-alive packets every 10 seconds to detect failure

```bash
autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "ssh_command"
```

### Run in the background, with no monitoring port and no remote shell, exiting if the port forward fails

```bash
autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L local_port:localhost:remote_port user@host
```

### Run in the background, logging `autossh` debug output and SSH verbose output to files

```bash
AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE=path/to/autossh_log_file.log autossh -f -M monitor_port -v -E path/to/ssh_log_file.log ssh_command
```

# supervisorctl

> Supervisor, a client/server system that allows its users to control a number of processes on UNIX-like operating systems. Supervisorctl is the command-line client piece of the supervisor which provides a shell-like interface. More information: <http://supervisord.org>.

## Examples

### Show the status of a process (or all processes if `process_name` is not specified)

```bash
supervisorctl status process_name
```

### Start/stop/restart a process

```bash
supervisorctl start|stop|restart process_name
```

### Start/stop/restart all processes in a group

```bash
supervisorctl start|stop|restart group_name:*
```

### Show last 100 bytes of process `stderr`

```bash
supervisorctl tail -100 process_name stderr
```

### Keep displaying `stdout` of a process

```bash
supervisorctl tail -f process_name stdout
```

### Reload process configuration file to add/remove processes as necessary

```bash
supervisorctl update
```

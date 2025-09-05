# emond

> Event Monitor service that accepts events from various services, runs them through a simple rules engine, and takes action. The actions can run commands, send email, or SMS messages. More information: <https://manpagez.com/man/8/emond/>.

## Examples

### Start the daemon

```bash
emond
```

### Specify rules for emond to process by giving a path to a file or directory

```bash
emond -r path/to/file_or_directory
```

### Use a specific configuration file

```bash
emond -c path/to/config_file
```

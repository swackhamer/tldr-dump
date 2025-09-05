# guacd

> Apache Guacamole proxy daemon. Support loader for client plugins to interface between the Guacamole protocol and any arbitrary remote desktop protocol (e.g. RDP, VNC, Other). More information: <https://manned.org/guacd>.

## Examples

### Bind to a specific port on localhost

```bash
guacd -b 127.0.0.1 -l 4823
```

### Start in debug mode, keeping the process in the foreground

```bash
guacd -f -L debug
```

### Start with TLS support

```bash
guacd -C my-cert.crt -K my-key.pem
```

### Write the PID to a file

```bash
guacd -p path/to/file.pid
```

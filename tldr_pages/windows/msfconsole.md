# msfconsole

> Console for the Metasploit Framework. More information: <https://docs.rapid7.com/metasploit/msf-overview>.

## Examples

### Launch the console

```bash
msfconsole
```

### Launch the console quietly without any banner

```bash
msfconsole [-q|--quiet]
```

### Do not enable database support

```bash
msfconsole [-n|--no-database]
```

### Execute console commands (Note: Use `;` for passing multiple commands)

```bash
msfconsole [-x|--execute-command] "use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run"
```

### Display help

```bash
msfconsole [-h|--help]
```

### Display version

```bash
msfconsole [-v|--version]
```

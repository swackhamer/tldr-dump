# searchsploit

> Search Exploit Database for exploits, shellcodes and/or papers. If known version numbers are used as search terms, exploits for both the exact version and others whose version range covers the one specified are shown. More information: <https://www.exploit-db.com/searchsploit>.

## Examples

### Search for an exploit, shellcode, or paper

```bash
searchsploit search_terms
```

### Search for a known specific version, e.g. sudo version 1.8.27

```bash
searchsploit sudo 1.8.27
```

### Show the exploit-db link to the found resources

```bash
searchsploit [-w|--www] search_terms
```

### Copy the resource to the current directory (requires the number of the exploit)

```bash
searchsploit [-m|--mirror] exploit_number
```

### Examine the resource, using the pager defined in the `$PAGER` environment variable

```bash
searchsploit [-x|--examine] exploit_number
```

### Update the local Exploit Database

```bash
searchsploit [-u|--update]
```

### Search for the [c]ommon [v]ulnerabilities and [e]xposures (CVE) value

```bash
searchsploit --cve 2021-44228
```

### Check results in `nmap`'s XML output with service version (`nmap -sV -oX nmap-output.xml`) for known exploits

```bash
searchsploit --nmap path/to/nmap-output.xml
```

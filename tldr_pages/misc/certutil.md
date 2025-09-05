# certutil

> Manage keys and certificates in both NSS databases and other NSS tokens. More information: <https://manned.org/certutil>.

## Examples

### Create a [N]ew certificate database in the current [d]irectory

```bash
certutil -N -d .
```

### List all certificates in a database

```bash
certutil -L -d .
```

### List all private [K]eys in a database specifying the password [f]ile

```bash
certutil -K -d . -f path/to/password_file.txt
```

### [A]dd the signed certificate to the requesters database specifying a [n]ickname, [t]rust attributes and an [i]nput CRT file

```bash
certutil -A -n "server_certificate" -t ",," -i path/to/file.crt -d .
```

### Add subject alternative names to a given [c]ertificate with a specific key size ([g])

```bash
certutil -S -f path/to/password_file.txt -d . -t ",," -c "server_certificate" -n "server_name" -g 2048 -s "CN=common_name,O=organization"
```

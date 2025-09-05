# mosquitto_passwd

> Manage password files for mosquitto. See also: `mosquitto`, the MQTT server that this manages. More information: <https://mosquitto.org/man/mosquitto_passwd-1.html>.

## Examples

### Add a new user to a password file (will prompt to enter the password)

```bash
mosquitto_passwd path/to/password_file username
```

### Create the password file if it doesn't already exist

```bash
mosquitto_passwd -c path/to/password_file username
```

### Delete the specified username instead

```bash
mosquitto_passwd -D path/to/password_file username
```

### Upgrade an old plain-text password file to a hashed password file

```bash
mosquitto_passwd -U path/to/password_file
```

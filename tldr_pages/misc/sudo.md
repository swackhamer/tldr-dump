# sudo

> Executes a single command as the superuser or another user. More information: <https://www.sudo.ws/sudo.html>.

## Examples

### Run a command as the superuser

```bash
sudo less /var/log/syslog
```

### Edit a file as the superuser with your default editor

```bash
sudo [-e|--edit] /etc/fstab
```

### Run a command as another user and/or group

```bash
sudo [-u|--user] user [-g|--group] group id -a
```

### Repeat the last command prefixed with `sudo` (only in Bash, Zsh, etc.)

```bash
sudo !!
```

### Launch the default shell with superuser privileges and run login-specific files (`.profile`, `.bash_profile`, etc.)

```bash
sudo [-i|--login]
```

### Launch the default shell with superuser privileges without changing the environment

```bash
sudo [-s|--shell]
```

### Launch the default shell as the specified user, loading the user's environment and reading login-specific files (`.profile`, `.bash_profile`, etc.)

```bash
sudo [-i|--login] [-u|--user] user
```

### List the allowed (and forbidden) commands for the invoking user

```bash
sudo [-ll|--list --list]
```

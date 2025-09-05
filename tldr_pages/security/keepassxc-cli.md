# keepassxc-cli

> Interface for KeePassXC. More information: <https://manned.org/keepassxc-cli>.

## Examples

### Search entries

```bash
keepassxc-cli search path/to/database_file name
```

### List the contents of a folder

```bash
keepassxc-cli ls path/to/database_file path/to/directory
```

### Add an entry with an auto-generated password

```bash
keepassxc-cli add [-g|--generate] path/to/database_file entry_name
```

### Delete an entry

```bash
keepassxc-cli rm path/to/database_file entry_name
```

### Copy an entry's password to the clipboard

```bash
keepassxc-cli clip path/to/database_file entry_name
```

### Copy a TOTP code to the clipboard

```bash
keepassxc-cli clip [-t|--totp] path/to/database_file entry_name
```

### Generate a passphrase with 7 words

```bash
keepassxc-cli diceware [-W|--words] 7
```

### Generate a password with 16 printable ASCII characters

```bash
keepassxc-cli generate [-lUns|--lower --upper --numeric --special] [-L|--length] 16
```

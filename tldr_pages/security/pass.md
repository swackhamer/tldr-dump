# pass

> Store and read passwords or other sensitive data. All data is GPG-encrypted, and managed with a Git repository. More information: <https://www.passwordstore.org>.

## Examples

### Initialize (or re-encrypt) the storage using one or more GPG IDs

```bash
pass init gpg_id_1 gpg_id_2
```

### Save a new password and additional information (press `<Ctrl d>` on a new line to complete)

```bash
pass insert [-m|--multiline] path/to/data
```

### Edit an entry

```bash
pass edit path/to/data
```

### Copy a password (first line of the data file) to the clipboard

```bash
pass [-c|--clip] path/to/data
```

### List the whole store tree

```bash
pass
```

### Generate a new random password with a given length, and copy it to the clipboard

```bash
pass generate [-c|--clip] path/to/data num
```

### Initialize a new Git repository (any changes done by pass will be committed automatically)

```bash
pass git init
```

### Run a Git command on behalf of the password storage

```bash
pass git command
```

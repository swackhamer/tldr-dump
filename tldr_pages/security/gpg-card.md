# gpg-card

> Administrate OpenPGP and PIV smart cards. Similar to `gpg --card-edit`. More information: <https://manned.org/gpg-card>.

## Examples

### Start in interactive mode

```bash
gpg-card
```

### Invoke one or more commands non-interactively

```bash
gpg-card command1 -- command2 -- command3
```

### Show information about a smart card

```bash
gpg-card list
```

### Retrieve the public key using the URL stored on an OpenPGP card

```bash
gpg-card fetch
```

### Set the URL used by the `fetch` command

```bash
gpg-card url
```

### Change or unblock PINs (uses the default action for the card in non-interactive mode)

```bash
gpg-card passwd
```

### Toggle the forcesig flag of an OpenPGP card (i.e. require entering the user PIN for signing)

```bash
gpg-card forcesig
```

### Factory reset a smart card (i.e. delete all data and reset PINs)

```bash
gpg-card factory-reset
```

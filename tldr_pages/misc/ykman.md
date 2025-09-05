# ykman

> YubiKey Manager - configure YubiKeys. If there are multiple YubiKeys connected, you have to add `--device serial_number` before a subcommand. More information: <https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

## Examples

### Display general information about a YubiKey (serial number, firmware version, capabilities, etc.)

```bash
ykman info
```

### List connected YubiKeys with short, one-line descriptions (including the serial number)

```bash
ykman list
```

### View documentation for enabling and disabling applications

```bash
tldr ykman config
```

### View documentation for managing the FIDO applications

```bash
tldr ykman fido
```

### View documentation for managing the OATH application

```bash
tldr ykman oath
```

### View documentation for managing the OpenPGP application

```bash
tldr ykman openpgp
```

# ykman-oath

> Manage the OATH YubiKey application. A `keyword` can be a part of the name or the issuer. More information: <https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>.

## Examples

### Display general information about the OATH application

```bash
ykman oath info
```

### Change the password used to protect OATH accounts (add `--clear` to remove it)

```bash
ykman oath access change
```

### Add a new account (the issuer is optional)

```bash
ykman oath accounts add [-i|--issuer] issuer name
```

### List all accounts (with their issuers)

```bash
ykman oath accounts list
```

### List all accounts with their current TOTP/HOTP codes (optionally filtering the list with a keyword)

```bash
ykman oath accounts code keyword
```

### Rename an account

```bash
ykman oath accounts rename keyword issuer:name|name
```

### Delete an account

```bash
ykman oath accounts delete keyword
```

### Delete all accounts and restore factory settings

```bash
ykman oath reset
```

# ykman-fido

> Manage YubiKey FIDO applications. More information: <https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>.

## Examples

### Display general information about the FIDO2 application

```bash
ykman fido info
```

### Change the FIDO pin

```bash
ykman fido access change-pin
```

### List resident credentials stored on the YubiKey

```bash
ykman fido credentials list
```

### Delete a resident credential from the YubiKey

```bash
ykman fido credentials delete id
```

### List fingerprints stored on the YubiKey (requires a key with a fingerprint sensor)

```bash
ykman fido fingerprints list
```

### Add a new fingerprint to the YubiKey

```bash
ykman fido fingerprints add name
```

### Delete a fingerprint from the YubiKey

```bash
ykman fido fingerprints delete name
```

### Wipe all FIDO credentials (you have to do this after exceeding the number of PIN retry attempts)

```bash
ykman fido reset
```

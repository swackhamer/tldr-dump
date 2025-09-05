# ykman-openpgp

> Manage the OpenPGP YubiKey application. Note: You need to use `gpg --card-edit` for some settings. More information: <https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>.

## Examples

### Display general information about the OpenPGP application

```bash
ykman openpgp info
```

### Set the number of retry attempts for the User PIN, Reset Code, and Admin PIN, respectively

```bash
ykman openpgp access set-retries 3 3 3
```

### Change the User PIN, Reset Code or Admin PIN

```bash
ykman openpgp access change-pin|reset-code|admin-pin
```

### Factory reset the OpenPGP application (you have to do this after exceeding the number of Admin PIN retry attempts)

```bash
ykman openpgp reset
```

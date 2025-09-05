# paperkey

> An OpenPGP key archiver. More information: <https://www.jabberwocky.com/software/paperkey/>.

## Examples

### Take a specific secret key and generate a text file with the secret data

```bash
paperkey --secret-key path/to/secret_key.gpg --output path/to/secret_data.txt
```

### Take the secret key data in `secret_data.txt` and combine it with the public key to reconstruct the secret key

```bash
paperkey --pubring path/to/public_key.gpg --secrets path/to/secret_data.txt --output secret_key.gpg
```

### Export a specific secret key and generate a text file with the secret data

```bash
gpg --export-secret-key key | paperkey --output path/to/secret_data.txt
```

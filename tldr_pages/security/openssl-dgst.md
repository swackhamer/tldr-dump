# openssl-dgst

> OpenSSL command to generate digest values and perform signature operations. More information: <https://www.openssl.org/docs/manmaster/man1/openssl-dgst.html>.

## Examples

### Calculate the SHA256 digest for a file, saving the result to a specific file

```bash
openssl dgst -sha256 -binary -out output_file input_file
```

### Sign a file using an RSA key, saving the result to a specific file

```bash
openssl dgst -sign private_key_file -sha256 -sigopt rsa_padding_mode:pss -out output_file input_file
```

### Verify an RSA signature

```bash
openssl dgst -verify public_key_file -signature signature_file -sigopt rsa_padding_mode:pss signature_message_file
```

### Sign a file using and ECDSA key

```bash
openssl dgst -sign private_key_file -sha256 -out output_file input_file
```

### Verify an ECDSA signature

```bash
openssl dgst -verify public_key_file -signature signature_file signature_message_file
```

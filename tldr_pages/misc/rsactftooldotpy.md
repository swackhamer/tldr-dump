# rsactftool.py

> RSA attack tool for CTF challenges - recover private keys from weak public keys and/or decrypt data. More information: <https://github.com/RsaCtfTool/RsaCtfTool>.

## Examples

### Recover a private key from a public key file

```bash
RsaCtfTool.py --publickey path/to/key.pub --private
```

### Decrypt a file using a public key

```bash
RsaCtfTool.py --publickey path/to/key.pub --decryptfile path/to/ciphered_file
```

### Decrypt a specific ciphertext string

```bash
RsaCtfTool.py --publickey path/to/key.pub --decrypt "ciphertext"
```

### Dump RSA key components (e.g., modulus, exponent) from a key file

```bash
RsaCtfTool.py --dumpkey --key path/to/key.pub
```

### Run a specific attack (e.g., Fermat factorization) to recover the private key

```bash
RsaCtfTool.py --publickey path/to/key.pub --private --attack fermat
```

### Generate a public key from modulus (n) and exponent (e)

```bash
RsaCtfTool.py --createpub -n modulus -e exponent
```

### Attempt all available attacks to recover the private key

```bash
RsaCtfTool.py --publickey path/to/key.pub --private --attack all
```

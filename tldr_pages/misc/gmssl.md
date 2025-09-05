# gmssl

> GmSSL is a crypto toolkit supporting SM1, SM2, SM3, SM4, SM9, and ZUC/ZUC256. More information: <http://gmssl.org/english.html>.

## Examples

### Generate an SM3 hash for a file

```bash
gmssl sm3 path/to/file
```

### Encrypt a file using the SM4 cipher

```bash
gmssl sms4 -e -in path/to/file -out path/to/file.sms4
```

### Decrypt a file using the SM4 cipher

```bash
gmssl sms4 -d -in path/to/file.sms4
```

### Generate an SM2 private key

```bash
gmssl sm2 -genkey -out path/to/file.pem
```

### Generate an SM2 public key from an existing private key

```bash
gmssl sm2 -pubout -in path/to/file.pem -out path/to/file.pem.pub
```

### Encrypt a file using the ZUC cipher

```bash
gmssl zuc -e -in path/to/file -out path/to/file.zuc
```

### Decrypt a file using the ZUC cipher

```bash
gmssl zuc -d -in path/to/file.zuc
```

### Display version

```bash
gmssl version
```

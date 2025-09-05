# sn

> Mono StrongName utility for signing and verifying IL assemblies. More information: <https://manned.org/sn>.

## Examples

### Generate a new StrongNaming key

```bash
sn -k path/to/key.snk
```

### Re-sign an assembly with the specified private key

```bash
sn -R path/to/assembly.dll path/to/key_pair.snk
```

### Show the public key of the private key that was used to sign an assembly

```bash
sn -T path/to/assembly.exe
```

### Extract the public key to a file

```bash
sn -e path/to/assembly.dll path/to/output.pub
```

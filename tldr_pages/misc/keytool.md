# keytool

> A certificate management utility included with Java. More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/keytool.html>.

## Examples

### Create a keystore

```bash
keytool -genkeypair -v -keystore path/to/file.keystore -alias key_name
```

### Change a keystore password

```bash
keytool -storepasswd -keystore path/to/file.keystore
```

### Change a key's password inside a specific keystore

```bash
keytool -keypasswd -alias key_name -keystore path/to/file.keystore
```

# apkleaks

> Expose URIs, endpoints, and secrets from APK files. Note: APKLeaks utilizes the `jadx` disassembler to decompile APK files. More information: <https://github.com/dwisiswant0/apkleaks>.

## Examples

### Scan an APK file for URIs, endpoints, and secrets

```bash
apkleaks [-f|--file] path/to/file.apk
```

### Scan and save the output to a specific file

```bash
apkleaks [-f|--file] path/to/file.apk [-o|--output] path/to/output.txt
```

### Pass `jadx` disassembler arguments

```bash
apkleaks [-f|--file] path/to/file.apk [-a|--args] "--threads-count 5 --deobf"
```

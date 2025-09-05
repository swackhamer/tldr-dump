# codesign

> Create and manipulate code signatures for macOS. More information: <https://keith.github.io/xcode-man-pages/codesign.1.html>.

## Examples

### Sign an application with a certificate

```bash
codesign --sign "My Company Name" path/to/application_file.app
```

### Verify the certificate of an application

```bash
codesign --verify path/to/application_file.app
```

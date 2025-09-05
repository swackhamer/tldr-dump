# bundletool

> Manipulate Android Application Bundles. Some subcommands such as `validate` have their own usage documentation. More information: <https://developer.android.com/tools/bundletool>.

## Examples

### Display help for a subcommand

```bash
bundletool help subcommand
```

### Generate APKs from an application bundle (prompts for keystore password)

```bash
bundletool build-apks --bundle path/to/bundle.aab --ks path/to/key.keystore --ks-key-alias key_alias --output path/to/file.apks
```

### Generate APKs from an application bundle giving the keystore password

```bash
bundletool build-apks --bundle path/to/bundle.aab --ks path/to/key.keystore --ks-key-alias key_alias --ks-pass pass:the_password --output path/to/file.apks
```

### Generate APKs including only one single APK for universal usage

```bash
bundletool build-apks --bundle path/to/bundle.aab --mode universal --ks path/to/key.keystore --ks-key-alias key_alias --output path/to/file.apks
```

### Install the right combination of APKs to an emulator or device

```bash
bundletool install-apks --apks path/to/file.apks
```

### Estimate the download size of an application

```bash
bundletool get-size total --apks path/to/file.apks
```

### Generate a device specification JSON file for an emulator or device

```bash
bundletool get-device-spec --output path/to/file.json
```

### Verify a bundle and display detailed information about it

```bash
bundletool validate --bundle path/to/bundle.aab
```

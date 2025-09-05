# bundletool-dump

> Manipulate Android Application Bundles. More information: <https://developer.android.com/tools/bundletool>.

## Examples

### Display the `AndroidManifest.xml` of the base module

```bash
bundletool dump manifest --bundle path/to/bundle.aab
```

### Display a specific value from the `AndroidManifest.xml` using XPath

```bash
bundletool dump manifest --bundle path/to/bundle.aab --xpath /manifest/@android:versionCode
```

### Display the `AndroidManifest.xml` of a specific module

```bash
bundletool dump manifest --bundle path/to/bundle.aab --module name
```

### Display all the resources in the application bundle

```bash
bundletool dump resources --bundle path/to/bundle.aab
```

### Display the configuration for a specific resource

```bash
bundletool dump resources --bundle path/to/bundle.aab --resource type/name
```

### Display the configuration and values for a specific resource using the ID

```bash
bundletool dump resources --bundle path/to/bundle.aab --resource 0x7f0e013a --values
```

### Display the contents of the bundle configuration file

```bash
bundletool dump config --bundle path/to/bundle.aab
```

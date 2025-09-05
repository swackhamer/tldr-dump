# fastlane

> Build and release mobile applications. More information: <https://docs.fastlane.tools/actions/>.

## Examples

### Build and sign the iOS application in the current directory

```bash
fastlane run build_app
```

### Run `pod install` for the project in the current directory

```bash
fastlane run cocoapods
```

### Delete the derived data from Xcode

```bash
fastlane run clear_derived_data
```

### Remove the cache for pods

```bash
fastlane run clean_cocoapods_cache
```

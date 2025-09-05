# fdroid

> F-Droid build tool. F-Droid is an installable catalog of FOSS (Free and Open Source Software) applications for the Android platform. More information: <https://f-droid.org/en/docs/Building_Applications/>.

## Examples

### Build a specific app

```bash
fdroid build app_id
```

### Build a specific app in a build server VM

```bash
fdroid build app_id --server
```

### Publish the app to the local repository

```bash
fdroid publish app_id
```

### Install the app on every connected device

```bash
fdroid install app_id
```

### Check if the metadata is formatted correctly

```bash
fdroid lint --format app_id
```

### Fix the formatting automatically (if possible)

```bash
fdroid rewritemeta app_id
```

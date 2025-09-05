# pio-pkg

> Manage packages in the registry. Packages can only be removed within 72 hours (3 days) from the date that they are published. More information: <https://docs.platformio.org/en/latest/core/userguide/package/>.

## Examples

### Create a package tarball from the current directory

```bash
pio pkg pack [-o|--output] path/to/package.tar.gz
```

### Create and publish a package tarball from the current directory

```bash
pio pkg publish
```

### Publish the current directory and restrict public access to it

```bash
pio pkg publish --private
```

### Publish a package

```bash
pio pkg publish path/to/package.tar.gz
```

### Publish a package with a custom release date (UTC)

```bash
pio pkg publish path/to/package.tar.gz --released-at "2021-04-08 21:15:38"
```

### Remove all versions of a published package from the registry

```bash
pio pkg unpublish package
```

### Remove a specific version of a published package from the registry

```bash
pio pkg unpublish package@version
```

### Undo the removal, putting all versions or a specific version of the package back into the registry

```bash
pio pkg unpublish --undo package@version
```

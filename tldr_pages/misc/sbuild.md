# sbuild

> Build a Debian binary package in a clean `chroot` environment. More information: <https://wiki.debian.org/sbuild>.

## Examples

### Build the package in the current directory

```bash
sbuild
```

### Build the given package

```bash
sbuild package
```

### Build for a certain distribution

```bash
sbuild --dist distribution
```

### Build using custom dependencies (if a directory is passed, all files ending with `.deb` are used)

```bash
sbuild --extra-package path/to/file_or_directory
```

### Run a shell in case of build failure to further investigate

```bash
sbuild --build-failed-commands=%SBUILD_SHELL
```

### Cross build for a certain architecture

```bash
sbuild --host architecture
```

### Build for the given native architecture

```bash
sbuild --arch architecture
```

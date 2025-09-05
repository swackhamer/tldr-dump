# conan

> The open source, decentralized and cross-platform package manager to create and share all your native binaries. Some subcommands such as `frogarian` have their own usage documentation. More information: <https://docs.conan.io/2/reference/commands.html>.

## Examples

### Install packages based on `conanfile.txt`

```bash
conan install .
```

### Install packages and create configuration files for a specific generator

```bash
conan install -g generator
```

### Install packages, building from source

```bash
conan install . --build
```

### Search for locally installed packages

```bash
conan search package
```

### Search for remote packages

```bash
conan search package -r remote
```

### List remotes

```bash
conan remote list
```

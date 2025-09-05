# komac

> Create WinGet manifests for the `winget-pkgs` repository. More information: <https://github.com/russellbanks/Komac>.

## Examples

### Create a new package from scratch

```bash
komac new Package.Identifier --version 1.2.3 --urls https://example.com/app.exe
```

### Update an existing package with a new version

```bash
komac update Package.Identifier --version 1.2.3 --urls https://example.com/app.exe
```

### Update a package with multiple URLs and automatically submit

```bash
komac update Package.Identifier --version 1.2.3 --urls https://example.com/app.exe https://example.com/app.msi ... --submit
```

### Remove a version from winget-pkgs

```bash
komac remove Package.Identifier --version 1.2.3
```

### List all versions for a package

```bash
komac list-versions Package.Identifier
```

### Sync your fork of winget-pkgs with the upstream repository

```bash
komac sync-fork
```

### Update the stored GitHub token

```bash
komac token update --token your_github_token
```

### Generate shell autocompletion script

```bash
komac complete bash|zsh|fish|powershell
```

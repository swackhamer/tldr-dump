# mist

> MIST - macOS Installer Super Tool. Automatically download macOS Firmwares/Installers. More information: <https://github.com/ninxsoft/mist-cli>.

## Examples

### List all available macOS Firmwares for Apple Silicon Macs

```bash
mist list firmware
```

### List all available macOS Installers for Intel Macs, including Universal Installers for macOS Big Sur and later

```bash
mist list installer
```

### List all macOS Installers that are compatible with this Mac, including Universal Installers for macOS Big Sur and later

```bash
mist list installer --compatible
```

### List all available macOS Installers for Intel Macs, including betas, also including Universal Installers for macOS Big Sur and later

```bash
mist list installer --include-betas
```

### List only the latest macOS Sonoma Installer for Intel Macs, including Universal Installers for macOS Big Sur and later

```bash
mist list installer --latest "macOS Sonoma"
```

### List and export macOS Installers to a CSV file

```bash
mist list installer --export "/path/to/export.csv"
```

### Download the latest macOS Sonoma Firmware for Apple Silicon Macs, with a custom name

```bash
mist download firmware "macOS Sonoma" --firmware-name "Install %NAME% %VERSION%-%BUILD%.ipsw"
```

### Download a specific macOS Installer version for Intel Macs, including Universal Installers for macOS Big Sur and later

```bash
mist download installer "13.5.2" application
```

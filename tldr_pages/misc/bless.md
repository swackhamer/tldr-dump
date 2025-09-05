# bless

> Set volume boot capability and startup disk options. More information: <https://keith.github.io/xcode-man-pages/bless.8.html>.

## Examples

### Bless a volume with only Mac OS X or Darwin, and create the BootX and `boot.efi` files as needed

```bash
bless --folder /Volumes/Mac OS X/System/Library/CoreServices --bootinfo --bootefi
```

### Set a volume containing either Mac OS 9 and Mac OS X to be the active volume

```bash
bless --mount /Volumes/Mac OS --setBoot
```

### Set the system to NetBoot and broadcast for an available server

```bash
bless --netboot --server bsdp://255.255.255.255
```

### Gather information about the currently selected volume (as determined by the firmware), suitable for piping to a program capable of parsing Property Lists

```bash
bless --info --plist
```

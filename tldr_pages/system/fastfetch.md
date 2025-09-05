# fastfetch

> Display information about your operating system, software and hardware. More information: <https://manned.org/fastfetch>.

## Examples

### Display system information

```bash
fastfetch
```

### Display full system information with all the modules enabled

```bash
fastfetch [-c|--config] all
```

### Load a custom configuration file

```bash
fastfetch [-c|--config] path/to/config_file
```

### Fetch a specific structure

```bash
fastfetch [-s|--structure] os:kernel:de:cpu:gpu
```

### Use a specific logo

```bash
fastfetch [-l|--logo] logo
```

### Display system information without a logo

```bash
fastfetch [-l|--logo] none
```

### Use a specific color for the keys and title

```bash
fastfetch --color blue
```

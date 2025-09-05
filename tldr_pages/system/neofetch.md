# neofetch

> Display information about your operating system, software and hardware. More information: <https://github.com/dylanaraps/neofetch>.

## Examples

### Return the default config, and create it if it's the first time the program runs

```bash
neofetch
```

### Trigger an info line from appearing in the output, where 'infoname' is the function name in the configuration file, e.g. memory

```bash
neofetch --enable|disable infoname
```

### Hide/Show OS architecture

```bash
neofetch --os_arch on|off
```

### Enable/Disable CPU brand in output

```bash
neofetch --cpu_brand on|off
```

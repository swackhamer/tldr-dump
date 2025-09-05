# nettacker

> Automate information gathering, vulnerability scanning and eventually generate a report. More information: <https://nettacker.readthedocs.io/en/latest/Home/>.

## Examples

### List all available modules

```bash
nettacker --show-all-modules
```

### Run a port scan on targets

```bash
nettacker [-m|--modules] port_scan [-i|--targets] 192.168.0.1/24,owasp.org,scanme.org,...
```

### Run a port scan on specific ports and targets listed in a file (newline separated)

```bash
nettacker [-m|--modules] port_scan [-g|--ports] 22,80,443,... [-l|--targets-list] path/to/targets.txt
```

### Run ping test before scan and then run multiple scan types on target

```bash
nettacker --ping-before-scan [-m|--modules] port_scan,subdomain_scan,waf_scan,... [-g|--ports] 80,443 [-i|--targets] owasp.org
```

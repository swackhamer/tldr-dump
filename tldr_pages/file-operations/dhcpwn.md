# dhcpwn

> Test DHCP IP exhaustion attacks and sniff local DHCP traffic. More information: <https://github.com/mschwager/dhcpwn>.

## Examples

### Flood the network with IP requests

```bash
dhcpwn [-i|--interface] network_interface flood [-c|--count] number_of_requests
```

### Sniff local DHCP traffic

```bash
dhcpwn [-i|--interface] network_interface sniff
```

# route

> Manually manipulate the routing tables. Requires root privileges. More information: <https://keith.github.io/xcode-man-pages/route.8.html>.

## Examples

### Add a route to a destination through a gateway

```bash
sudo route add "destination_ip_address" "gateway_address"
```

### Add a route to a /24 subnet through a gateway

```bash
sudo route add "subnet_ip_address/24" "gateway_address"
```

### Run in test mode (does not do anything, just print)

```bash
sudo route -t add "destination_ip_address/24" "gateway_address"
```

### Remove all routes

```bash
sudo route flush
```

### Delete a specific route

```bash
sudo route delete "destination_ip_address/24"
```

### Lookup and display the route for a destination (hostname or IP address)

```bash
sudo route get "destination"
```

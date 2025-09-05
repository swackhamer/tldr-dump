# openvpn

> OpenVPN client and daemon binary. More information: <https://openvpn.net/community-docs/community-articles/openvpn-2-6-manual.html>.

## Examples

### Connect to server using a configuration file

```bash
sudo openvpn path/to/client.conf
```

### Try to set up an insecure peer-to-peer tunnel on bob.example.com host

```bash
sudo openvpn --remote alice.example.com --dev tun1 --ifconfig 10.4.0.1 10.4.0.2
```

### Connect to the awaiting bob.example.com host without encryption

```bash
sudo openvpn --remote bob.example.com --dev tun1 --ifconfig 10.4.0.2 10.4.0.1
```

### Create a cryptographic key and save it to file

```bash
openvpn --genkey secret path/to/key
```

### Try to set up a peer-to-peer tunnel on bob.example.com host with a static key

```bash
sudo openvpn --remote alice.example.com --dev tun1 --ifconfig 10.4.0.1 10.4.0.2 --secret path/to/key
```

### Connect to the awaiting bob.example.com host with the same static key as on bob.example.com

```bash
sudo openvpn --remote bob.example.com --dev tun1 --ifconfig 10.4.0.2 10.4.0.1 --secret path/to/key
```

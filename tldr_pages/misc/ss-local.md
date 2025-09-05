# ss-local

> Run a Shadowsocks client as a SOCKS5 proxy. More information: <https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>.

## Examples

### Run a Shadowsocks proxy by specifying the host, server port, local port, password, and encryption method

```bash
ss-local -s host -p server_port -l local port -k password -m encrypt_method
```

### Run a Shadowsocks proxy by specifying the configuration file

```bash
ss-local -c path/to/config/file.json
```

### Use a plugin to run the proxy client

```bash
ss-local --plugin plugin_name --plugin-opts plugin_options
```

### Enable TCP fast open

```bash
ss-local --fast-open
```

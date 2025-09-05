# bgpgrep

> Filter and print BGP data within MRT dumps. Can read files compressed with `gzip`, `bzip2` and `xz`. More information: <https://codeberg.org/1414codeforge/ubgpsuite>.

## Examples

### List all routes

```bash
bgpgrep master6.mrt
```

### List routes received from a specific peer, determined by the peer's AS number

```bash
bgpgrep master4.mrt -peer 64498
```

### List routes received from a specific peer, determined by the peer's IP address

```bash
bgpgrep master4.mrt.bz2 -peer 2001:db8:dead:cafe:acd::19e
```

### List routes which have certain ASNs in their AS path

```bash
bgpgrep master6.mrt.bz2 -aspath '64498 64510'
```

### List routes that lead to a specific address

```bash
bgpgrep master6.mrt.bz2 -supernet '2001:db8:dead:cafe:aef::5'
```

### List routes that have communities from a specific AS

```bash
bgpgrep master4.mrt -communities \( '64497:*' \)
```

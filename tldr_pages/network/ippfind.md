# ippfind

> Find services registered with a DNS server or available through local devices. See also: `ipptool`, `ippeveprinter`. More information: <https://openprinting.github.io/cups/doc/man-ippfind.html>.

## Examples

### List IPP printers registered on the network with their status

```bash
ippfind [-l|--ls]
```

### Send a specific PostScript document to every PostScript printer on the network

```bash
ippfind --txt-pdl application/postscript [-x|--exec] ipptool -f path/to/document.ps '{}' print-job.test \;
```

### Send a PostScript test document to every PostScript printer on the network

```bash
ippfind --txt-pdl application/postscript [-x|--exec] ipptool -f onepage-letter.ps '{}' print-job.test \;
```

### Send a PostScript test document to every PostScript printer on the network, whose name matches a `regex`

```bash
ippfind --txt-pdl application/postscript [-h|--host] regex [-x|--exec] ipptool -f onepage-letter.ps '{}' print-job.test \;
```

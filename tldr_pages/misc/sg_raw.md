# sg_raw

> Send arbitrary SCSI command to a connected device. More information: <https://manned.org/sg_raw>.

## Examples

### Send a command to an optical SCSI device assigned to `sr0` to load the media in its tray

```bash
sg_raw /dev/sr0 EA 00 00 00 00 01
```

### Read data from `IFILE` instead of `stdin`

```bash
sg_raw [-i|--infile] path/to/IFILE /dev/sgX SCSI_command
```

### Skip the first `LEN` bytes of input data

```bash
sg_raw [-k|--skip] LEN /dev/sgX SCSI_command
```

### Read `SLEN` bytes of data and send to the device

```bash
sg_raw [-s|--send] SLEN /dev/sgX SCSI_command
```

### Wait up to `SEC` seconds for `sg_raw` to finish processing

```bash
sg_raw [-t|--timeout] SEC /dev/sgX SCSI_command
```

### Increase verbosity level by 1

```bash
sg_raw [-v|--verbose] /dev/sgX SCSI_command
```

### Dump returned data in binary form

```bash
sg_raw [-b|--binary] /dev/sgX SCSI_command
```

### Write data received from the specified device to an `OFILE`

```bash
sg_raw [-o|--outfile] path/to/OFILE /dev/sgX SCSI_command
```

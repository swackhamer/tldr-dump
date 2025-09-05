# isisdl

> A downloading utility for ISIS of TU-Berlin. Download all your files and videos from ISIS. More information: <https://github.com/Emily3403/isisdl>.

## Examples

### Start the synchronization process

```bash
isisdl
```

### Limit the download rate to 20 MiB/s and download with 5 threads

```bash
isisdl --download-rate 20 --max-num-threads 5
```

### Run the initialization configuration wizard

```bash
isisdl --init
```

### Run the additional configuration wizard

```bash
isisdl --config
```

### Initiate a full synchronization of the database and compute the checksum of every file

```bash
isisdl --sync
```

### Start ffmpeg to compress downloaded videos

```bash
isisdl --compress
```

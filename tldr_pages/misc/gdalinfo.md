# gdalinfo

> List various information about a GDAL supported raster dataset. More information: <https://gdal.org/programs/gdalinfo.html>.

## Examples

### List all supported raster formats

```bash
gdalinfo --formats
```

### List information about a specific raster dataset

```bash
gdalinfo path/to/input.tif
```

### List information about a specific raster dataset in JSON format

```bash
gdalinfo -json path/to/input.tif
```

### Show histogram values of a specific raster dataset

```bash
gdalinfo -hist path/to/input.tif
```

### List information about a Web Map Service (WMS)

```bash
gdalinfo WMS:https://services.meggsimum.de/geoserver/ows
```

### List information about a specific dataset of a Web Map Service (WMS)

```bash
gdalinfo WMS:https://services.meggsimum.de/geoserver/ows -sd 4
```

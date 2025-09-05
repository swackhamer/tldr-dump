# gdal_contour

> Create contour lines and polygons from a digital elevation model. More information: <https://gdal.org/programs/gdal_contour.html>.

## Examples

### Create a vector dataset with contour lines spread over an 100-meter [i]nterval while [a]ttributing the elevation property as "ele"

```bash
gdal_contour -a ele -i 100.0 path/to/input.tif path/to/output.gpkg
```

### Create a vector dataset with [p]olygons spread over an 100-meter [i]nterval

```bash
gdal_contour -i 100.0 -p path/to/input.tif path/to/output.gpkg
```

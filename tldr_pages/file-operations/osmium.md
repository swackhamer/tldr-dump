# osmium

> Multipurpose tool for handling OpenStreetMap (OSM) files. More information: <https://osmcode.org/osmium-tool/manual>.

## Examples

### Show file information

```bash
osmium fileinfo path/to/input.osm
```

### Display contents

```bash
osmium show path/to/input.osm
```

### Convert file format from PBF into XML

```bash
osmium cat path/to/input.osm.pbf [-o|--output] path/to/output.osm
```

### Extract a geographic region by the given [b]ounding box

```bash
osmium extract [-b|--bbox] min_longitude,min_latitude,max_longitude,max_latitude path/to/input.pbf [-o|--output] path/to/output.pbf
```

### Extract a geographic region by a GeoJSON file

```bash
osmium extract [-p|--polygon] path/to/polygon.geojson path/to/input.pbf [-o|--output] path/to/output.pbf
```

### Filter all objects tagged as "restaurant"

```bash
osmium tags-filter path/to/input.pbf amenity=restaurant [-o|--output] path/to/output.pbf
```

### Filter for "way" objects tagged as "highway"

```bash
osmium tags-filter path/to/input.pbf w/highway [-o|--output] path/to/output.pbf
```

### Filter "way" and "relation" objects tagged as "building"

```bash
osmium tags-filter path/to/input.pbf wr/building [-o|--output] path/to/output.pbf
```

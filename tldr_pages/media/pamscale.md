# pamscale

> Scale a Netpbm image. More information: <https://netpbm.sourceforge.net/doc/pamscale.html>.

## Examples

### Scale an image such that the result has the specified dimensions

```bash
pamscale [-wid|-width] width [-h|-height] height path/to/input.pam > path/to/output.pam
```

### Scale an image such that the result has the specified width, keeping the aspect ratio

```bash
pamscale [-wid|-width] width path/to/input.pam > path/to/output.pam
```

### Scale an image such that its width and height is changed by the specified factors

```bash
pamscale [-xsc|-xscale] x_factor [-ysc|-yscale] y_factor path/to/input.pam > path/to/output.pam
```

### Scale an image such that it fits into the specified bounding box while preserving its aspect ratio

```bash
pamscale -xyfit bbox_width bbox_height path/to/input.pam > path/to/output.pam
```

### Scale an image such that it completely fills the specified box while preserving its aspect ratio

```bash
pamscale -xyfill box_width box_height path/to/input.pam > path/to/output.pam
```

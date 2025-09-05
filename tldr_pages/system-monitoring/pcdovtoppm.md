# pcdovtoppm

> Create an index image for a photo CD based on its overview file. More information: <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

## Examples

### Create a PPM index image from a PCD overview file

```bash
pcdovtoppm path/to/file.pcd > path/to/output.ppm
```

### Specify the maximum width of the output image and the maximum size of each of the images contained in the output

```bash
pcdovtoppm [-m|-maxwidth] width [-s|-size] size path/to/file.pcd > path/to/output.ppm
```

### Specify the maximum number of images across and the maximum number of colours

```bash
pcdovtoppm [-a|-across] n_images [-c|-colors] n_colours path/to/file.pcd > path/to/output.ppm
```

### Use the specified font for annotations and paint the background white

```bash
pcdovtoppm [-f|-font] font [-w|-white] path/to/file.pcd > path/to/output.ppm
```

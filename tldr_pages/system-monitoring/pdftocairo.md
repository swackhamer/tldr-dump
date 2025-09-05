# pdftocairo

> Convert PDF files to PNG/JPEG/TIFF/PDF/PS/EPS/SVG using cairo. More information: <https://manned.org/pdftocairo>.

## Examples

### Convert a PDF file to JPEG

```bash
pdftocairo path/to/file.pdf -jpeg
```

### Convert to PDF expanding the output to fill the paper

```bash
pdftocairo path/to/file.pdf output.pdf -pdf -expand
```

### Convert to SVG specifying the first/last page to convert

```bash
pdftocairo path/to/file.pdf output.svg -svg -f first_page -l last_page
```

### Convert to PNG with 200ppi resolution

```bash
pdftocairo path/to/file.pdf output.png -png -r 200
```

### Convert to grayscale TIFF setting paper size to A3

```bash
pdftocairo path/to/file.pdf -tiff -gray -paper A3
```

### Convert to PNG cropping x and y pixels from the top-left corner

```bash
pdftocairo path/to/file.pdf -png -x x_pixels -y y_pixels
```

# ppmntsc

> Make the RGB colors in a PPM image compatible with NTSC or PAL color systems. More information: <https://netpbm.sourceforge.net/doc/ppmntsc.html>.

## Examples

### Make the RGB colors in a PPM image compatible with NTSC color systems

```bash
ppmntsc path/to/input_file.ppm > path/to/output_file.ppm
```

### Make the RGB colors in a PPM image compatible with PAL color systems

```bash
ppmntsc --pal path/to/input_file.ppm > path/to/output_file.ppm
```

### Print the number of illegal pixels in the input image to `stderr`

```bash
ppmntsc [--verb|--verbose] path/to/input_file.ppm > path/to/output_file.ppm
```

### Output only legal/illegal/corrected pixels, set other pixels to black

```bash
ppmntsc --legalonly|illegalonly|correctedonly path/to/input_file.ppm > path/to/output_file.ppm
```

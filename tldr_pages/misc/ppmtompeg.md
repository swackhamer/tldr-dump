# ppmtompeg

> Encode an MPEG-1 stream. More information: <https://netpbm.sourceforge.net/doc/ppmtompeg.html>.

## Examples

### Produce an MPEG-1 stream using the parameter file to specify inputs and outputs

```bash
ppmtompeg path/to/parameter_file
```

### Encode the GOP with the specified number only

```bash
ppmtompeg [-g|-gop] gop_num path/to/parameter_file
```

### Specify the first and last frame to encode

```bash
ppmtompeg [-fr|-frames] first_frame last_frame path/to/parameter_file
```

### Combine multiple MPEG frames into a single MPEG-1 stream

```bash
ppmtompeg -combine_frames path/to/parameter_file
```

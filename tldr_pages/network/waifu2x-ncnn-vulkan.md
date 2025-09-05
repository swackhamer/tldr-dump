# waifu2x-ncnn-vulkan

> Image upscaler for manga/anime-style images using NCNN neural network framework. More information: <https://github.com/nihui/waifu2x-ncnn-vulkan>.

## Examples

### Upscale an image

```bash
waifu2x-ncnn-vulkan -i path/to/input_file -o path/to/output_file
```

### Upscale an image by a custom scale factor and denoise it

```bash
waifu2x-ncnn-vulkan -i path/to/input_file -o path/to/output_file -s 1|2|4|8|16|32 -n -1|0|1|2|3
```

### Save the upscaled image in a specific format

```bash
waifu2x-ncnn-vulkan -i path/to/input_file -o path/to/output_file -f jpg|png|webp
```

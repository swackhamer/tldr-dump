# pamstack

> Stack the planes of multiple PAM images into one PAM image. More information: <https://netpbm.sourceforge.net/doc/pamstack.html>.

## Examples

### Stack the planes of the specified PAM images in the specified order

```bash
pamstack path/to/image1.pam path/to/image2.pam ... > path/to/output.pam
```

### Specify the tuple type name of the output PAM file (maximum of 255 characters)

```bash
pamstack [-t|-tupletype] tuple_type path/to/image1.pam path/to/image2.pam ... > path/to/output.pam
```

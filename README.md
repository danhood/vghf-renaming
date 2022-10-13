# VGHF Image Renumberer

## Overview / Usage

Renumbers images in an interleaved fashion as per [Frank's Tweet][renumbering]. The script `renumber.py` copies (and
renumbers) images from `<input directory>` into `<output directory>`.

Usage: `python renumber.py <input directory> <output directory>`

```
$ python renumber.py input output
input/image_0001.tif => output/image_0001.tif
input/image_0002.tif => output/image_0032.tif
input/image_0003.tif => output/image_0002.tif
input/image_0004.tif => output/image_0031.tif
input/image_0005.tif => output/image_0003.tif
input/image_0006.tif => output/image_0030.tif
input/image_0007.tif => output/image_0004.tif
input/image_0008.tif => output/image_0029.tif
input/image_0009.tif => output/image_0005.tif
input/image_0010.tif => output/image_0028.tif
input/image_0011.tif => output/image_0006.tif
input/image_0012.tif => output/image_0027.tif
input/image_0013.tif => output/image_0007.tif
input/image_0014.tif => output/image_0026.tif
input/image_0015.tif => output/image_0008.tif
input/image_0016.tif => output/image_0025.tif
input/image_0017.tif => output/image_0009.tif
input/image_0018.tif => output/image_0024.tif
input/image_0019.tif => output/image_0010.tif
input/image_0020.tif => output/image_0023.tif
input/image_0021.tif => output/image_0011.tif
input/image_0022.tif => output/image_0022.tif
input/image_0023.tif => output/image_0012.tif
input/image_0024.tif => output/image_0021.tif
input/image_0025.tif => output/image_0013.tif
input/image_0026.tif => output/image_0020.tif
input/image_0027.tif => output/image_0014.tif
input/image_0028.tif => output/image_0019.tif
input/image_0029.tif => output/image_0015.tif
input/image_0030.tif => output/image_0018.tif
input/image_0031.tif => output/image_0016.tif
input/image_0032.tif => output/image_0017.tif
```

## Assumptions / Limitations

- Script checks for correct number of arguments
- Script copies files (it does not rename in place)
- Script checks for an even number of images in order to follow this scheme
- Script checks for any missing image numbers
- Script assumes `<output directory>` does not exist

## Dependencies

This script should run (without external dependencies) within a Python 3.6+ environment.

## Testing

The following generates sample numbered test images. From a UNIX-based shell (assumes [ImageMagick][imagemagick]
installed, and bash-like shell)...

```
mkdir test
for i in $(seq -f "%04g" 1 32); do
    convert -fill black -pointsize 256 label:$i test/image_$i.tif;
done
```

[imagemagick]: https://imagemagick.org/
[renumbering]: https://twitter.com/frankcifaldi/status/1579521687573626881

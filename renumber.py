#!/usr/bin/env python

import glob
import os
import shutil
import sys

# error check - abort if wrong number of arguments
if len(sys.argv) != 3:
    sys.exit(f'Usage: {sys.argv[0]} <input directory> <output directory>')

# grab all image_XXXX.tif images in source directory
images = glob.glob(os.path.join(sys.argv[1], 'image_*.tif'))

# error check - abort if any missing images
for i in range(1, len(images) + 1):
    image = os.path.join(sys.argv[1], f'image_{i:04}.tif')
    if not os.path.exists(image):
        sys.exit(f'Error: missing "{image}"')

# error check - abort if not an even number of images
if len(images) % 2:
    sys.exit('Error: not an even number of images')

# start odd numbers at 1 (as we're counting up - 1, 2, 3, 4, ...)
odd_counter = 1

# start even numbers at max (as we're counting down - 32, 31, 30, 29, ...)
even_counter = len(images)

# error check - abort if output directory already exists
if os.path.exists(sys.argv[2]):
    sys.exit(f'Error: output directory "{sys.argv[2]}" already exists')

# create output directory
os.mkdir(sys.argv[2])

# walk though images, copying as we go
for i in range(1, len(images) + 1):

    # odd page - count up
    if i % 2:
        dest = odd_counter
        odd_counter += 1

    # even page - count down
    else:
        dest = even_counter
        even_counter -= 1

    # generate source and dest filenames
    src = os.path.join(sys.argv[1], f'image_{i:04}.tif')
    dest = os.path.join(sys.argv[2], f'image_{dest:04}.tif')

    # uncomment below to output renumbering
    print(f'{src} => {dest}')

    # copy (and rename) preserving as much file attributes as possible
    shutil.copy2(src, dest)

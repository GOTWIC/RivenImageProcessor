# Riven Image Processor
A program that takes multiple riven screenshots, applies multiple hue transfers, and ultimately edits them into a collage.

### Prerequisites
To use the program, you need to install some packages and programs.

In the command line or bash, you need to type:

``` pip install Pillow ```

Next install ImageMagick from the following link:

https://imagemagick.org/script/download.php

### Requirements
 - A folder called **Raw**
 - A folder called **Output**
 - Images must be 1920x1080
 - Images must be uneditedand uncropped
 - Your background should be the Corpus theme. The hue transfers are optimized for the Corpus theme/background. Results with other backgrounds may vary.

### Running the Program

Add your screenshots in the **Raw** folder. Then just run _RivenImageProcessor.py_. You can do this by double clicking on the file. In the output folder, you will see the cropped and edited rivens individually, as well as the collage of all the rivens.



# Riven Image Processor
A program that takes multiple riven screenshots, applies multiple hue transfers, and after some further editing, turns them into a collage.

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

### Customizing the Program

It is mandatory to set the path inside the program, as well as set the dimensions of the final collage.

On line 65, change the rootPath variable to the location where the project folder is downloaded.

On line 75 and 76, change the dimensions of the final collage. For example, if you have 18 rivens, you can make it 6 columns and 3 rows. Avoid a prime number of rivens.

##### Other Customizations

You can change how much spacing you want between the rivens by changing the margin value in lines 70-73. The greater the margins, the smaller the space between rivens.

You can also change the color of the rivens by editing lines 21-23. The default value is green, but I have commented the values you need to change to create red, blue, green, and gold.




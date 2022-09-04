afrom PIL import Image
import math
import os
from os.path import exists

editedRivens = []

def changeColor(img):
    width = img.size[0]
    height = img.size[1]
    for i in range(0,width):
        for j in range(0,height):
            data = img.getpixel((i,j))
            r = data[0]
            g = data[1]
            b = data[2]

            # DEFAULT NUMBERS: 110, 90, 135
            # GOLD: 125, 100, 70
            # GREEN: 75, 100, 75
            # BLUE: 65, 95, 100
            # RED: 175, 95, 95
            red_modifier = 65
            green_modifier = 95
            blue_modifier = 100

            if (r <= 35) and (g <= 41) and (b <= 50):
                if j < 365:
                    img.putpixel((i,j),(32,33,36))
                else:
                    img.putpixel((i,j),(42,43,48))
            elif (b > r) and (b > math.ceil(1.2*g)) and (b < 2*r):
                img.putpixel((i,j),(math.ceil(r*red_modifier/110), math.ceil(g*green_modifier/90), math.ceil(b*blue_modifier/135)))
                #img.putpixel((i,j),(255,255,255))
            
            elif (g > b*0.4) or (b > r) or (g > r*0.5) or (r > 4*g):
                bw = int(math.ceil((r+g+b)/3))
                img.putpixel((i,j),(bw,bw,bw))

            if isBackground(i,j,r,g,b):
                img.putpixel((i,j),(42,43,48,1))

    #img.show()

    return img
def isBackground(i,j,r,g,b):
    if(i >= 27) and (i <= 263) and (j >= 25) and (j <= 370):
        return False
    else:
        #if (abs(r - g) <= 5) or (abs(r - b) <= 5) or (abs(g - b) <= 10):
        #    return False
        if (g > r + 20) or (g > b + 20):
            return True
        else:
            return False    
def cropImage(img, leftMargin, rightMargin, topMargin, bottomMargin):
    width, height = img.size
    img = img.crop((leftMargin, topMargin, width - rightMargin, height - bottomMargin))
    return img

#def concatImages(columns, rows, imgName, outPath):



    #os.chdir(outPath)
    #if exists(imgName):
    #    os.remove(imgName)
    #os.system("magick montage -mode concatenate -tile " + str(columns) + "x" + str(rows) + " *.jpg " + imgName)

def to2DList(imgList1D):
    imgList2D = []
    for i in range(0, len(imgList1D), columns):
        imgList2D.append(imgList1D[i:i+columns])
    return imgList2D

def concatImages(columns, rows, imgName, outPath):
    #for each image in the directory outPath, add to the list of size columns*rows
    imgList1D = []
    for image in os.listdir(outPath):
        if (image.endswith(".JPG")):
            imgList1D.append(image)
    imgList2D = to2DList(imgList1D)

def create_collage():
    cols = 4
    rows = 4
    thumbnail_width, thumbnail_height  = editedRivens[0].size
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (thumbnail_width * cols, thumbnail_height * rows))
    ims = []
    for p in editedRivens:
        im = p
        im.thumbnail(size)
        ims.append(im)
    i = 0
    x = 0
    y = 0
    for col in range(cols):
        for row in range(rows):
            print(i, x, y)
            new_im.paste(ims[i], (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    new_im.save("Collage.jpg")




rootPath = "C:/Users/shoum/Downloads/RivenImageProcessor-main/"

inPath = rootPath + "RivenImageProcessor-main/Raw"
outPath = rootPath + "RivenImageProcessor-main/Output"

leftMargin = 815  
rightMargin = 815
topMargin = 350
bottomMargin = 335

rows = 4
columns = 4

finalImageName = "Final.jpg"

for imagePath in os.listdir(inPath):
        inputPath = os.path.join(inPath, imagePath)
        fullOutPath = os.path.join(outPath, imagePath)
        img = changeColor(cropImage(Image.open(inputPath), leftMargin, rightMargin, topMargin, bottomMargin))
        img.save(fullOutPath)
        editedRivens.append(img)

#concatImages(columns, rows, finalImageName, outPath)

create_collage()

#Image.open(outPath + "/" + finalImageName).show()

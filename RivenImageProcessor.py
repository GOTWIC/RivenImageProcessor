from PIL import Image
import math
import os
from os.path import exists

def changeColor(img):
    width = img.size[0]
    height = img.size[1]
    for i in range(0,width):# process all pixels
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

    img.show()

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
def concatImages(columns, rows, imgName):
    os.chdir("C:/users/swagn/downloads/RivenCollection/Output")
    if exists(imgName):
        os.remove(imgName)
    os.system("magick montage -mode concatenate -tile " + str(columns) + "x" + str(rows) + " *.jpg " + imgName)


inPath = "C:/Users/swagn/downloads/RivenCollection/Raw2"
outPath = "C:/Users/swagn/downloads/RivenCollection/Output"

leftMargin = 815  
rightMargin = 815
topMargin = 350
bottomMargin = 335

rows = 1
columns = 2

finalImageName = "Final.jpg"

for imagePath in os.listdir(inPath):
        inputPath = os.path.join(inPath, imagePath)
        fullOutPath = os.path.join(outPath, imagePath)
        img = changeColor(cropImage(Image.open(inputPath), leftMargin, rightMargin, topMargin, bottomMargin))
        img.save(fullOutPath)

#concatImages(columns, rows, finalImageName)

#Image.open("C:/users/swagn/downloads/RivenCollection/Output/" + finalImageName).show()






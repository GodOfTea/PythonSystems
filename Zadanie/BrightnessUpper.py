from PIL import Image, ImageDraw

img = Image.open("noise.png")
draw = ImageDraw.Draw(img)
width = img.size[0]
height = img.size[1]
pix = img.load()

imgCopy = img.copy()

for i in range(0, width-1):
    if i-1 > 0 and i < width:
        for j in range(0, height-1):
            if j-1 > 0 and j < height:
                p1 = pix[i-1, j-1][0] + pix[i-1, j-1][1] + pix[i-1, j-1][2]
                p2 = pix[i-1, j][0] + pix[i-1, j][1] + pix[i-1, j][2]
                p3 = pix[i-1, j+1][0] + pix[i-1, j+1][1] + pix[i-1, j+1][2]
                p4 = pix[i, j-1][0] + pix[i, j-1][1] + pix[i, j-1][2]
                local = pix[i, j][0] + pix[i, j][1] + pix[i, j][2]
                p6 = pix[i, j+1][0] + pix[i, j+1][1] + pix[i, j+1][2]
                p7 = pix[i+1, j-1][0] + pix[i+1, j-1][1] + pix[i+1, j-1][2]
                p8 = pix[i+1, j][0] + pix[i+1, j][1] + pix[i+1, j][2]
                p9 = pix[i+1, j+1][0] + pix[i+1, j+1][1] + pix[i+1, j+1][2]
                localAll = (p1+p2+p3+p4+p6+p7+p8+p9)/8
                if local == 0:
                    local = 1
                if local < localAll:
                    imgCopy.putpixel((i, j),
                                     (int(pix[i, j][0]*localAll/local),
                                      int(pix[i, j][1]*localAll/local),
                                      int(pix[i, j][2]*localAll/local)))

imgCopy.save("BrightnessUpperFilter.png", "PNG")
del draw


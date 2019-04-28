from PIL import Image, ImageDraw

img = Image.open("noise.png")
draw = ImageDraw.Draw(img)
width = img.size[0]
height = img.size[1]
pix = img.load()

imgCopy = img.copy()

for i in range(1, width - 1):
    for j in range(1, height - 1):
        Cnw = [pix[i - 1, j - 1][0], pix[i - 1, j - 1][1], pix[i - 1, j - 1][2]]
        Cn = [pix[i - 1, j][0], pix[i - 1, j][1], pix[i - 1, j][2]]
        Cne = [pix[i - 1, j + 1][0], pix[i - 1, j + 1][1], pix[i - 1, j + 1][2]]
        Cw = [pix[i, j - 1][0], pix[i, j - 1][1], pix[i, j - 1][2]]
        C = [pix[i, j][0], pix[i, j][1], pix[i, j][2]]
        Ce = [pix[i, j + 1][0], pix[i, j + 1][1], pix[i, j + 1][2]]
        Csw = [pix[i + 1, j - 1][0], pix[i + 1, j - 1][1], pix[i + 1, j - 1][2]]
        Cs = [pix[i + 1, j][0], pix[i + 1, j][1], pix[i + 1, j][2]]
        Cse = [pix[i + 1, j + 1][0], pix[i + 1, j + 1][1], pix[i + 1, j + 1][2]]

        R = int((Cnw[0] + Cn[0] + Cne[0] + Cw[0] + Ce[0] + Csw[0] + Cs[0] + Cse[0])/8)
        G = int((Cnw[1] + Cn[1] + Cne[1] + Cw[1] + Ce[1] + Csw[1] + Cs[1] + Cse[1])/8)
        B = int((Cnw[2] + Cn[2] + Cne[2] + Cw[2] + Ce[2] + Csw[2] + Cs[2] + Cse[2])/8)

        imgCopy.putpixel((i, j), (R, G, B))

imgCopy.save("AverageV2.png", "PNG")
del draw
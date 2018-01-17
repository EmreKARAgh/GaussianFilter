from PIL import Image
import numpy
im = Image.open("source.jpg")
w,h=im.size
pix=numpy.zeros(shape=(w, h, 3),dtype=numpy.uint8)
matris=numpy.zeros(shape=(w, h, 3),dtype=numpy.uint8)
neighbormatrice = numpy.zeros(shape=(5, 5))#Neighbor matrice to be filtered pixel
for i in range(w):  #Get and assign image's RGB values
   for j in range(h):
        rgb_im = im.convert('RGB')
        r , g , b = rgb_im.getpixel((i, j))
        pix[i][j] =r, g, b
        if (i >= 2 & i < (w - 2) & j >= 2 & j < (h - 2)):
            for m in range(3):
                toplam = 0.0
                for k in range(5):
                    for l in range(5):
                        neighbormatrice[k][l] = matris[k + i - 2][l + j - 2][m]#Create neighbor matrice's indexs(exclude a frame size=2)
                for k in range(5):
                    for l in range(5):
                        toplam = (toplam + (neighbormatrice[k][l] * 0.04))#0.04 is filter value.
                matris[j][i][m] = int(toplam)
img = Image.fromarray(matris, 'RGB')#Create an image with RGB values
img.save('target.jpg')
img.show()

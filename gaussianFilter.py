import image
import PIL
import numpy
from PIL import Image, ImageMath
def filtering(matris):
    neighbormatrice = numpy.zeros(shape=(5, 5))#komsuluk matrisi
    filtermatrice = [[1, 4, 6, 4, 1],#filtreleme referans matrisi(assagida elemanlar 256'ya bölünecektir)
                     [4, 16, 24, 16, 4],
                     [6, 24, 36, 24, 6],
                     [4, 16, 36, 24, 6],
                     [1, 4, 6, 4, 1]]
    for k in range(5):
        for l in range(5):
            filtermatrice[k][l] = filtermatrice[k][l] / 256
    toplam = 0.0
    """""
    YUMUSATMA YAPILIRKEN RESMİN ETRAFINDAN 2 PİKSEL GENİSLİGİNDE BİR CERCEVE İHMAL EDİLMİSTİR.
    """
    for i in range(2, w - 2):
        for j in range(2, h - 2):
            for k in range(5):#Pikseller icin komsuluk matrisi olusturulur
                for l in range(5):
                    neighbormatrice[k][l] = matris[k + i - 2][l + j - 2]
            for k in range(5):##komsuluk matrisi filtreleme matrisiyle işleme sokulur
                for l in range(5):
                    toplam = toplam + (neighbormatrice[k][l] * filtermatrice[k][l])
            matris[i][j] = toplam#islem sonucu yumusatmanin yapildigi pikselin degerine esitlenir
    return matris
#Resim import edilir
im = Image.open("indir.jpg")
#resmin boyutları
w=259
h=194
#resmi dijitallestirerek, R degerleri icin bir matris olusturur
red = numpy.zeros(shape = (w , h))
for i in range(w):
   for j in range(h):
        rgb_im = im.convert('RGB')
        r , g , b = rgb_im.getpixel((i, j))
        red[i][j]=r
#resmi dijitallestirerek, G degerleri icin bir matris olusturur
green = numpy.zeros(shape = (w , h))
for i in range(w):
   for j in range(h):
        rgb_im = im.convert('RGB')
        r , g , b = rgb_im.getpixel((i, j))
        green[i][j]=g
#resmi dijitallestirerek, B degerleri icin bir matris olusturur
blue = numpy.zeros(shape = (w , h))
for i in range(w):
   for j in range(h):
        rgb_im = im.convert('RGB')
        r , g , b = rgb_im.getpixel((i, j))
        blue[i][j]=b
#R,G,B degerlerini iceren matrisler sırayla filtreleme fonksiyonuna gönderilip,fonksiyon cıktısına esitlenir
red=filtering(red)
print(red[29][142])
green=filtering(green)
blue=filtering(blue)
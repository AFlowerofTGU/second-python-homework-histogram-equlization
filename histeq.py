# python implementation of image histogram equalization 
from PIL import Image
import numpy as np
def CalcHistEqMapping( hist, n):
    # n is the total number of pixels in the image
    # hist is a list containing histogram information or an numpy array for the same purpose
    lut = np.zeros(256)
    s = 0
    for i in range(0, 256):
        s += hist[i]
        lut[i] = 255. * s / n
    lut = np.uint8(lut)
    return lut

def HistEq( f ): # f is numpy array or an Image object
    hist_f,_ = np.histogram(f.ravel(), bins=256)

    size = f.shape
    n = size[0] * size[1]

    lut = CalcHistEqMapping(hist_f, n)

    # g = np.array( f )
    # g = g.ravel()
    #
    # for i in range( len(g) ):
    #    x = g[i]
    #    g[i] = lut[x]
    #
    # g = g.reshape( (size[0], size[1]) )
    g = np.array(f)
    g = lut[g]

    return g


def ReadImage(fn):
    # img = cv2.imread(fn,cv2.IMREAD_UNCHANGED)
    img = Image.open(fn)
    img = img.convert("L")
    img1 = np.array(img)
    return img1


def main(fn1,fn2):
    f = ReadImage(fn1)
    g = HistEq(f)
    g = Image.fromarray(g)
    g.save(fn2+"he-splash"+".png")

if __name__ == '__main__':
    root1 = "./splash.png"
    root2 = "C:/Users/86183/PycharmProjects/shadow_xtraction/histogram-equalization/"
    main(root1,root2)

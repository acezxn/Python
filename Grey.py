from PIL import Image
import numpy as np
ima = input("Insert image name: ")
im = Image.open('my.png')
np_im = np.array(im)
x = 0
le = int(input("insert length: "))
wi = int(input("insert width: "))
for i in range(le):
    for a in range(wi):
        R = np_im[x,a][0]
        G = np_im[x,a][1]
        B = np_im[x,a][2]
        Y = int(0.299 * R + 0.587 * G + 0.114 * B)
        np_im[x,a] = [Y,Y,Y]
        print(Y)
    x += 1

img = Image.fromarray(np_im, 'RGB')
img.show()

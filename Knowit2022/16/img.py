from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

giraffe_im = plt.imread("giraffe.png")
harambe_im = plt.imread("harambe.png")

im_size = giraffe_im.shape


newIm = np.zeros_like(giraffe_im)

channel = 0

for row in range(0, im_size[0]):
    for col in range(0, im_size[1]):
       # newIm[row][col] = (int(giraffe_im[row][col][channel]
        #                       * 255) & int(harambe_im[row][col][channel] * 255)) / 255
        newIm[row][col] = int(bin(int(giraffe_im[row][col][channel] * 255)
                                  )[-1]) | int(bin(int(harambe_im[row][col][channel] * 255))[-1])

plt.imshow(newIm, cmap="gray")
plt.show()

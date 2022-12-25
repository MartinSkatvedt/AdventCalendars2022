from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
im_1 = Image.open("Svalbard1.png").convert("L")
im_2 = Image.open("Svalbard2.png").convert("L")

data_1 = np.asarray(im_1)
data_2 = np.asarray(im_2)


new = data_2 - data_1 

plt.imshow(new, cmap="gray")
plt.show()
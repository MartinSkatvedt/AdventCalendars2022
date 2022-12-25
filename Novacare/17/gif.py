from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

gif = Image.open("input.gif", )

newIm = np.asarray(gif).copy()
for frame in range(1,gif.n_frames):
    gif.seek(frame)
    newIm += np.asarray(gif.convert("L"))

plt.imshow(newIm, cmap="gray")
plt.show()
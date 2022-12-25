from matplotlib import pyplot as plt

img = []
with open("encrypted.txt") as f:
    for line in f.readlines():
        img.append(line.split())


newImg = img.copy()
for row_index, row in enumerate(img):
    for column_index, value in enumerate(row):
        if bin(int(value)).count("1") % 2 == 0:
            newImg[row_index][column_index] = 0
        else:
            newImg[row_index][column_index] = 1

plt.imshow(newImg, cmap="gray")
plt.show()
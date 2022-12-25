from PIL import Image

giraffe_im = Image.open('giraffe.png') 
harambe_im = Image.open('harambe.png') 
g_pix = giraffe_im.load()
h_pix = harambe_im.load()


newIm = Image.new("L", giraffe_im.size)
newImData = newIm.load()
channel = 0

for row in range(0, giraffe_im.size[0]):
    for col in range(0, giraffe_im.size[1]):
        g_pix_val = g_pix[row, col][channel]
        h_pix_val = h_pix[row, col][channel]
        newImData[row, col]= g_pix_val & h_pix_val 


newIm.show()


from os import walk
from exif import Image
from matplotlib import pyplot as plt

filenames = next(walk("./pokemon"), (None, None, []))[2]
img_coords= list()

for filename in filenames:
    img_path = "./pokemon/"+ filename
    with open(img_path, 'rb') as src:
        img = Image(src)
 
        lat = (float(img.gps_latitude[0]) + float(img.gps_latitude[1])/60 + float(img.gps_latitude[1])/(60*60)) 
        long = (float(img.gps_longitude[0]) + float(img.gps_longitude[1])/60 + float(img.gps_longitude[1])/(60*60)) 

        img_coords.append([lat, long])


plt.scatter(*zip(*img_coords))
plt.show()

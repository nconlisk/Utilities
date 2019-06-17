########################################################
#                                                      #
#                Author: Noel Conlisk                  #
#               Email: noecon@gmail.com                #
#                                                      #
########################################################


import os
import io
from PIL import Image

path = os.getcwd()

images = [f for f in os.listdir(path) if f.endswith('.tif')]

for i in images:
    im = Image.open(i)
    imName = i.split('.')[0]
    im.save(imName+'.jpg')

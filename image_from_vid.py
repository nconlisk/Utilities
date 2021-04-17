import sys
import argparse
import os

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut, filename):
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    framesTotal = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    selector = 20
    print(framesTotal)
    count = 0
    folderOut = "\\" + filename.split(".")[0]
   
                   
    success = True
    while success:
        frameID = int(round(vidcap.get(1)))
        print(frameID)
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        if frameID%selector==0:
            print ('Writing frame_%d.jpg' % frameID)
            cv2.imwrite( pathOut + folderOut + "\\frame%d.jpg" % frameID, image)     # save frame as JPEG file
            count += 1
    print('Number of images generated: %d'%count)

if __name__=="__main__":
    filename = "shoe.mp4" #input("Enter video file including extension to be reconstructed: ")
    path = os.getcwd()
    pathIn = path + "\\" + filename 
    pathOut = path
    extractImages(pathIn, pathOut, filename)

# Need to also write out camera/lens metadata.
# Make who thing work with interactive gui
# Add textboxes to input frame number, add delay in script so can see total frame number,
# add video preview window, add start and stop sliders.

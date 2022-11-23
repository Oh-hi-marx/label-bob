import cv2
import numpy as np
import math
import os
import shutil

from tool.files import *
from tool.videos import *

inputPath = "./inputs"
labelPath = "./segmentLabels"

outputPath = "./outputs"
labelsOutPath = "./labels.txt"

segmentLength = 99999999999999

try:
    os.mkdir(outputPath)
except:
    pass

videos = onlyfolders(inputPath)
videoLabels = onlyfiles(labelPath)
with open(labelsOutPath, 'w') as f:
    pass
f.close()

for videoLabel in videoLabels:
    labels =[]
    print(videoLabel)
    with open(videoLabel) as f:
        lines = f.readlines()
        for line in lines:
            labels.append(line.replace("\n",""))
    print("Labels: ",labels)
    frames =[]
    frames = natSort(onlyfiles(inputPath + "/" + videoLabel.split("/")[-1].split(".txt")[0]))
    print("Found %i frames"%len(frames))
    for segi, segment in enumerate(labels):
        start = int(segment.split(" ")[0])
        end = int(segment.split(" ")[1])
        classN = segment.split(" ")[2]
        print(segment)
        counter = start
        segN = 0
        countFromZero =0
        while(counter< end+1 and  counter <= end):
            if((counter-start)%(segmentLength ) == 0):
                framePath = outputPath +"/" +videoLabel.split("/")[-1].split(".txt")[0] + "-"+str(segi)+"-"+str(segN)
                f= open(labelsOutPath, "a")
                print(counter,countFromZero,end,)
                f.write(framePath+" " + str(min(end-counter, segmentLength)) +" " + str(classN) + "\n")
                f.close()
                try:
                    os.mkdir(framePath )
                except:
                    pass
                #print("n")
                segN +=1
            #print(counter, segN)
            if(countFromZero<10):
                fileName = "img_0000" + str(countFromZero) + ".jpg"
            elif(countFromZero<100):
                fileName = "img_000" + str(countFromZero) + ".jpg"
            elif(countFromZero<1000):
                fileName = "img_00" + str(countFromZero) + ".jpg"
            shutil.copyfile(frames[counter],framePath + "/" + fileName)

            #print(frames[counter],framePath + "/" + fileName)
            counter+=1
            countFromZero +=1
        #print("")

import cv2
import numpy as np
import os
from threading import Thread
import time
from tool.files import *

maxPreload = 20000
skipFrames = 60
inputPath = "./inputs"
outputPath = "./segmentLabels"

try:
    os.mkdir(outputPath)
except:
    pass
videos = onlyfolders(inputPath)
print("Found %i videos"%len(videos))



class preloadFrames():
    def __init__(self):
        self.frames = []
        self.stopLoad = 0

    def preloadFrames(self,frames):
        print("Preloading frames, may take a few seconds!")
        for frame in frames:
            if(self.stopLoad==1):
                break
            self.frames.append(cv2.imread(frame))

    def run(self, frames):
        p = Thread(target=self.preloadFrames, args = (frames,))
        p.start()

if __name__ == "__main__":
    for vid in videos:
        frames = natSort(onlyfiles(vid))

        preloadFrame = preloadFrames()
        if(len(frames)<maxPreload):

            preloadFrame.run(frames)
        frameN = 0

        labelList = []
        start =-1
        currentClass = "0"
        while(1):

            if(len(frames)==len(preloadFrame.frames)):
                frame = preloadFrame.frames[frameN]
            else:
                frame = cv2.imread(frames[frameN])
            frame = cv2.resize(frame, (1500,800))
            cv2.imshow("", frame)

            k = cv2.waitKey(0)
            print(k)
            if(k==27): #esc to exit
                break

            elif(k==100 and frameN + 1 < len(frames)): #right arrow
                frameN+=1
            elif(k==97 and frameN > 1): #left arrow
                frameN-=1
            elif(k==101 and frameN + skipFrames < len(frames)): #e skip
                frameN+=skipFrames
            elif(k==113 and frameN > skipFrames): #q skip
                frameN-=skipFrames
            elif(k==115 ): #down arrow
                start = frameN
            elif(k==119 ): #up arrow
                if(frameN > start and start != -1):
                    labelList.append((start,frameN, int(currentClass)))
                    print("Adding to list [start, end, class] ", (start,frameN, int(currentClass)))
            elif(k>47 and k<58): #number keys - set class number
                if(len(currentClass)>0):
                    if(currentClass[0]=="0"):
                        currentClass = currentClass[1:-1]
                print(chr(k))
                currentClass = currentClass + chr(k)
            elif(k==8 and len(currentClass)>0):  #delete key - delete class number
                currentClass = currentClass[0:len(currentClass)-1]
            elif(k==122):#z - undo last clip
                if(len(labelList)>0):
                    labelList.pop()
                    print("Remove last segment")

            print(frameN, labelList, currentClass)
        txtPath = outputPath+ "/"+ vid.split("/")[-1]+".txt"
        print(txtPath)
        with open(txtPath, 'w') as f:
            print(88)
            for line in labelList:
                f.write(str(line).replace(",","").replace("(","").replace(")","")+"\n")
        f.close()
        preloadFrame.stopLoad =1
        del preloadFrame

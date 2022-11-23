import cv2
import numpy as np
import os
from threading import Thread
import time
from tool.files import *
outputX = 1800;outputY = 1000
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

def putText(img, text, org = (10,10),color = (155, 125, 30), fontScale = 1.3, thickness = 1):
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, text, org, font,
                    fontScale, color, thickness, cv2.LINE_AA)
def trackLabeledFrames(alreadyLabeledFrames, start, end, classN):
    a = list(range(start, end))
    alreadyLabeledFrames.append(a)
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
        alreadyLabeledFrames = []
        labelList = []
        start =-1
        currentClass = "0"
        saveMessage = ""
        while(1):
            #load frame from memory or disk
            if(len(frames)==len(preloadFrame.frames)):
                frameNew = preloadFrame.frames[frameN]
            else:
                frameNew = cv2.imread(frames[frameN])
            #put informational text
            frame = frameNew.copy()

            for alreadyLabeled in alreadyLabeledFrames:
                if( frameN in alreadyLabeled):
                    putText (frame, "ALREADY LABELED", (int(outputX/5), int(outputY/2)), color = (0,2,255), fontScale = 5, thickness = 5)
            putText (frame, "Frame: %i" %(frameN), (int(outputX/1.1), int(outputY/15)), color = (0,255,1))
            putText (frame, "Class: %s"%(currentClass), (int(outputX/1.1), int(outputY/10)), color = (0,255,1))
            if(saveMessage!= ""):
                putText(frame, saveMessage, (int(outputX/5), int(outputY/3)),  (0,255,1),3,2)
            saveMessage = ""
            frame = cv2.resize(frame, (outputX, outputY))
            cv2.imshow("", frame)

            k = cv2.waitKey(0)

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
                saveMessage="Set start at frame %i"%start
            elif(k==119 ): #up arrow
                if(frameN > start and start != -1 and currentClass!=""):
                    labelList.append((start,frameN, int(currentClass)))
                    trackLabeledFrames(alreadyLabeledFrames, start,frameN, int(currentClass))
                    saveMessage = "Added frame %i:%i (class %i)"%(start, frameN, int(currentClass))
                    print("Adding to list [start, end, class] ", (start,frameN, int(currentClass)))
            elif(k>47 and k<58): #number keys - set class number
                if(len(currentClass)>0):
                    if(currentClass[0]=="0"):
                        currentClass = currentClass[1:-1]

                currentClass = currentClass + chr(k)
            elif(k==8 and len(currentClass)>0):  #delete key - delete class number
                currentClass = currentClass[0:len(currentClass)-1]
            elif(k==122):#z - undo last clip
                if(len(labelList)>0):
                    labelList.pop()
                    saveMessage = "Removed last segment %i:%i (class %i)"%(start, frameN, int(currentClass))
                    print("Remove last segment")

            print(labelList)
        labelList = list(dict.fromkeys(labelList))
        txtPath = outputPath+ "/"+ vid.split("/")[-1]+".txt"
        print(txtPath)
        with open(txtPath, 'w') as f:
            print(88)
            for line in labelList:
                f.write(str(line).replace(",","").replace("(","").replace(")","")+"\n")
        f.close()
        preloadFrame.stopLoad =1
        del preloadFrame

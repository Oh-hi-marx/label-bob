import cv2
import numpy as np
import time
import os
from multiprocessing import Process,  Value

from tool.files import *
from tool.videos import *

inputPath = "./downloads"
outputPath = "inputs"
numThreads = 10
try:
	os.mkdir(outputPath)
except:
	pass
files = onlyfiles(inputPath)

def extractVideoFrames(file, outputPath,y):
	outDir = outputPath + "/" + file.split("/")[-1].split(".")[0]
	try:
		os.mkdir(outDir )
	except:
		pass
	extractFrames(file,outDir ,resolution = (1080,1920), letterBox = 1)
	y.value -=1


y = Value('i', 0)
print(y.value)

while(len(files)>0):
	if(y.value < numThreads):
		y.value +=1
		file = files.pop()
		print(file)
		Process(target = extractVideoFrames, args = (file, outputPath, y,)).start()

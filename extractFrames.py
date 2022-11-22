import cv2
import numpy as np

import os

from tool.files import *
from tool.videos import *

inputPath = "./downloads"
outputPath = "inputs"
files = onlyfiles(inputPath)
for file in files:
	outDir = outputPath + "/" + file.split("/")[-1].split(".")[0]
	try:
		os.mkdir(outDir )
	except:
		pass
	extractFrames(file,outDir ,resolution = (1080,1920))
    

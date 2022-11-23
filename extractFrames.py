import os
from multiprocessing import Process,  Value
from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *

inputPath = "./downloads"
outputPath = "inputs"
numThreads = 2
processes = []

try:
    os.mkdir(outputPath)
except:
    pass
files = onlyfiles(inputPath)

y = Value('i', 0)

def extractVideoFrames(file, outputPath,y):
	outDir = outputPath + "/" + file.split("/")[-1].split(".")[0]
	try:
		os.mkdir(outDir)
	except:
		pass
	extractFrames(file,outDir ,resolution = (1080,1920), letterBox = 1)
	y.value -=1




if __name__ == '__main__':
    threads =[]
    # while(len(files)>0):
    for i in tqdm(range(len(files))):
        if(y.value < numThreads):
            y.value +=1
            file = files.pop()
            process = Process(target = extractVideoFrames, args = (file, outputPath, y,))
            process.start()
            threads.append(process)
            # process.join()
    for t in threads:
        t.join()

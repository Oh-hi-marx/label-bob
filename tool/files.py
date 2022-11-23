import os
from os import listdir
from os.path import isfile, join
import shutil
import re

	
def onlyfiles(mypath):
	onlyfiles = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]
	return onlyfiles
	
def onlyfolders(mypath):
	folders = next(os.walk(mypath))[1]
	for i,folder in enumerate(folders):
		folders[i] = join(mypath,folder)
	return folders
	
def removeAllFiles(mypath):
	shutil.rmtree(mypath)
	
def natSort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


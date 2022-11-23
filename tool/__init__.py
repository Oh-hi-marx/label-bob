from os import listdir
from os.path import isfile, join

def onlyfiles(mypath):
	onlyfiles = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]
	return onlyfiles

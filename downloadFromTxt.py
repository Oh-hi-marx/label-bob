import os
try:
    os.mkdir("downloads")
except:
    pass
path = input("txt file name? (dont include .txt): ")
urls = []
#read txt file
with open(path+".txt") as f:
    contents = f.readlines()
for line in contents:
    urls.append(line)
#remove duplicates
res = []
[res.append(x) for x in urls if x not in res]
urls = res
print(urls)
print("Found %i urls" %len(urls))

currentDir = os.getcwd()
for url in urls:
	command = "yt-dlp -o '" + currentDir+"/downloads/%(id)s.%(ext)s'"  +' ' + url
	print(command)
	print("\nDownloading ", url)
	os.system(command)
	print("=============")

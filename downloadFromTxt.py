import os

path = input("txt file name? (dont include .txt): ")
urls = []
#read txt file
with open(path+".txt") as f:
    contents = f.read()
    urls.append(contents)
#remove duplicates
list(dict.fromkeys(urls))

print("Found %i urls" %len(urls))

currentDir = os.getcwd()
for url in urls:
	command = "yt-dlp -o '" + currentDir+"/downloads/%(title)s.%(ext)s'"  +' ' + url
	print("\nDownloading ", url)
	os.system(command) 

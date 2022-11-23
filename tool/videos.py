
import os
import cv2
import numpy as np
def letterbox_image(image, size):
    '''resize image with unchanged aspect ratio using padding'''
    iw, ih = image.shape[0:2][::-1]
    w, h = size
    scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)
    image = cv2.resize(image, (nw,nh), interpolation=cv2.INTER_CUBIC)
    new_image = np.zeros((size[1], size[0], 3), np.uint8)
    new_image.fill(128)
    dx = (w-nw)//2
    dy = (h-nh)//2
    new_image[dy:dy+nh, dx:dx+nw,:] = image
    return new_image
def extractFrames(inpath, outpath, resolution = (1080,1920), letterBox =0):
	# Create a VideoCapture object and read from input file
	# If the input is the camera, pass 0 instead of the video file name

	cap = cv2.VideoCapture(inpath)

	# Check if camera opened successfully
	if (cap.isOpened()== False):
	  print("Error opening video stream or file")

	# Read until video is completed
	counter=0
	while(cap.isOpened()):
	  # Capture frame-by-frame
	  ret, frame = cap.read()
	  if ret == True:
		  if(frame.shape[0:2]!=resolution and letterBox ==1):
			  frame = letterbox_image(frame, [1920,1080])
		  #cv2.imshow('Frame',frame)
		  cv2.imwrite(outpath+ "/" + str(counter)+".jpg", frame)
		  counter+=1
		  #if cv2.waitKey(25) & 0xFF == ord('q'):
		#	  break
	  else:
      		break
	cap.release()
	cv2.destroyAllWindows()

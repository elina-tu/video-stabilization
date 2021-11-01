# -*- coding: utf-8 -*-

import numpy as np
import cv2
 
#Gets input video 
clip = cv2.VideoCapture('clip1.mp4')
 
#Gets frame count
n_frames = int(clip.get(cv2.CAP_PROP_FRAME_COUNT))
 
#Gets width and height of video
w = int(clip.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(clip.get(cv2.CAP_PROP_FRAME_HEIGHT))

#frames per second
fps = 30
#VideoWriter object used to create the new video
#fourcc is the video codec
#fps is the frames per second and w,h are the width and height of the final video
#The 0 is needed to save the video as greyscale
output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), fps, (w,h), 0)

#loops through each frame
while(True):
    #gets the next frame of the video, ret = return value. will return false if there are no more frames to read
    ret, frame = clip.read()
    if ret == True:
        #this converts the frame to a numpy array. either this or the frame object could
        #be passed to another program for processing?
        test = np.asarray(frame)
        #converts frame to greyscale and adds it to the new video
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        output.write(grey_frame)
        
        #this line can be used to show each frame as it processes
        cv2.imshow("Live",grey_frame)
        #this part can be used to stop the process by pressing the q key
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break 
clip.release()
output.release()

cv2.destroyAllWindows()


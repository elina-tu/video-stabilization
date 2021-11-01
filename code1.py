# -*- coding: utf-8 -*-

import cv2

def crop(test, width_left, width_right, height_top, height_bottom):
    '''Function that selects a rectangular section of the frame'''
    new_frame = test[int(height_top*h):int((1 - height_bottom)*h), \
        int(width_left*w):int((1 - width_right)*w)]
    return new_frame

def new_size(width_left, width_right, height_top, height_bottom):
    """Calculate height and wodth of cropped frame"""
    new_w = int((1 - width_right)*w) - int(width_left*w)
    new_h = int((1 - height_bottom)*h) - int(height_top*h)
    return new_w, new_h

#Gets input video 
clip = cv2.VideoCapture('clip1.mp4')
 
#Gets frame count
n_frames = int(clip.get(cv2.CAP_PROP_FRAME_COUNT))
 
#Gets width and height of video
w = int(clip.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(clip.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cropping parrameters as a fraction of original height/width
width_left = 0.2
width_right = 0.2
height_top = 0.3
height_bottom = 0.2

#new frame size
new_w, new_h = new_size(width_left, width_right, height_top, height_bottom)

#frames per second
fps = 30
#VideoWriter object used to create the new video
#fourcc is the video codec
#fps is the frames per second and w,h are the width and height of the final video
#The 0 is needed to save the video as greyscale
output = cv2.VideoWriter('crop_output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), fps, (new_w, new_h), 0)

#loops through each frame
while(True):
    #gets the next frame of the video, ret = return value. will return false if there are no more frames to read
    ret, frame = clip.read()
    if ret == True:
        #crop frame
        new_frame = crop(frame, width_left, width_right, height_top, height_bottom)
        #converts frame to greyscale and adds it to the new video
        grey_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
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


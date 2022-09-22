# importing packages
import cv2
import numpy as np

# function to rename the uploaded original image
# takes in the uploaded image as input and renames
# def ogRename():
#     pass

# # function to rename the uploaded template
# def tempRename():
#     pass
# # reading the input upload original image

# OR? can we open the uploaded image directly 

# read the original image
im_rgb = cv2.imread('real.jpg')

# convert the real image into Gray scale
im_gray = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2GRAY)


# reading the template in gray scale mode
temp = cv2.imread('template.jpg', 0)

# reading the width and height
# using -1 to invert the output as the 
# output comes in the format of h,w.
w, h = temp.shape[::-1]

# matching template
res = cv2.matchTemplate(im_gray, temp, cv2.TM_CCOEFF_NORMED)
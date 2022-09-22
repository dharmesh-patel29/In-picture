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

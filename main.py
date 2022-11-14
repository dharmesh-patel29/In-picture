# importing packages
import cv2
import numpy as np

from kivy.lang import Builder
from kivymd.app import MDApp

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

# setting the threshold (matching accuracy)
# for now this value is manually set
# later on it will be read by an object from frontend
threshold = 0.80

# locating pixels only above the threshold matching
loc = np.where( res>=threshold)  # setting condition


# using zip, making w,h format for a point
# then using for loop, going to each point
# and drawing yellow boxes around them.

# to get the dimension of the box: we will use
# same dimensions of the template. We take a point
# and the box will be of the same width and height
# of that of the template.
# also making boxes inside the original images (in-place)
for pt in zip(*loc[::-1]):
    cv2.rectangle(im_rgb, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

# function to display the image containing object when needed
def dispObj():
    
    # resizing the output image according to the MDcard
    ims = cv2.resize(im_rgb, (480,480))
    cv2.imshow('Object found', ims)


dispObj()

# below code stops the python kernel from crashing
cv2.waitKey(0) 

cv2.destroyAllWindows()

class MyApp(MDApp): 
    



    def build(self):
        self.theme_cls.theme_style = "Light"
        # loading my.kv file    # going to screenmanager
        return  Builder.load_file("myapp.kv") 
    



# if its the main file, execute the following code
if __name__ == "__main__":
    MyApp().run()
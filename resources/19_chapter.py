# Step 1 - import libraries
import cv2 as cv
import numpy as np

# step 2 - Define a function
def find_coord(event, x,y,flags,params):
    if event == cv.EVENT_FLAG_LBUTTON:
        # Left click mouse
        print(x, '', y)
        # How to define or print on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x) + "," + str(y), (x,y), font, 1, (255.0,0), thickness=2)
        # show the test image and imag eitself
        cv.imshow("image", img)

# Final funtion to read and dispaly

if __name__=="__main__":
    # reading an iamge
    img = cv.imread("resources/warp.jpg",1)
    # display the image
    cv.imshow("image",img)
    #  setting call back function
    cv.setMouseCallback("image",find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()
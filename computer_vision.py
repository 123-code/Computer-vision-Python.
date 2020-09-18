import numpy as np
import cv2

# reading images
img = cv2.imread("/Users/naran/OneDrive/Desktop/opencv-logo.png")

#creating named windows

cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
#show the image,specify window and image name.
cv2.imshow("Image",img)

#specify waiting time
cv2.waitKey(0)

#write image back to file.
cv2.imwrite("output.jpg",img)
